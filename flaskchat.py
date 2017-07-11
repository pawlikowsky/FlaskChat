from flask import Flask, render_template, session, url_for, request, redirect, abort, jsonify
from random import choice
from string import ascii_letters
from forms import LoginForm, WorkspaceForm, JoinForm
from models import Chat, User, db
from flask_socketio import SocketIO, join_room, leave_room, send, emit


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.username = 'admin'
app.password = 'password'
socketio = SocketIO(app)


@app.teardown_appcontext
def shutdiwb_session(exception=None):
    db.session.remove()


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        chat_uid = ''.join(choice(ascii_letters) for i in range(12))
        room = Chat(chat_uid, form.language.data)
        user = User(form.username.data)
        db.session.add(room)
        db.session.add(user)
        db.session.commit()

        print('added db entry')
        session['logged_in'] = True
        session['chat_uid'] = chat_uid
        session['username'] = request.form['username']
        return redirect(url_for('czat', chat_uid=chat_uid))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    username = session['username']
    session.pop('username', None)
    session.pop('logged_in', None)
    print('user ' + username + ' logout')
    return redirect(url_for('login'))


@app.route('/join/<chat_uid>', methods=['GET', 'POST'])
def join(chat_uid):
    form = JoinForm()
    if form.validate_on_submit() and request.method == 'POST':
        print('redirect for ' + chat_uid)
        session['logged_in'] = True
        session['username'] = request.form['username']
        session['chat_uid'] = chat_uid
        return redirect(url_for('czat', chat_uid=chat_uid))
    return render_template('join.html', form=form, chat_uid=chat_uid)


@app.route('/id/<chat_uid>', methods=['GET', 'POST'])
def czat(chat_uid):
    if not session.get('logged_in'):
        return redirect(url_for('join', chat_uid=chat_uid))
    user = session['username']
    q = Chat.query.filter_by(chat_uid=chat_uid).first()
    content = q.content
    editor = q.editor
    if q == None:
        print("q not found")
        return redirect(url_for('index'))
    form = WorkspaceForm()
    # if form.validate_on_submit():
    #     data = form.workspace.data
    #     q.content = data
    #     db.session.commit()
    #     print('workspace added')
    return render_template('workspace.html', chat_uid=chat_uid, user=user, form=form, content=content, editor=editor)


@app.route('/id/<chat_uid>/add', methods=['GET', 'POST'])
def czat_add(chat_uid):
    q = Chat.query.filter_by(chat_uid=chat_uid).first()
    form = WorkspaceForm()
    if form.validate_on_submit():
        data = form.workspace.data
        q.content = data
        db.session.commit()
        print('workspace added')
        return jsonify(data={'message': '{}'.format(form.workspace.data)})
    return jsonify(data=form.errors)


@app.route('/id/<chat_uid>/workspace', methods=['GET', 'POST'])
def czat_workspace(chat_uid):
    q = Chat.query.filter_by(chat_uid=chat_uid).first()
    workspace = q.content
    return jsonify(data={'workspace': workspace})


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('chat_uid')
    join_room(room)
    emit('status', {'msg': session.get('username') + ' connected'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('chat_uid')
    join_room(room)
    emit('message', {'msg':'<span class="badge grey">'+  session.get('username') + '</span> ' + message['msg'] }, room=room)


@socketio.on('workspace', namespace='/chat')
def workspace(message):
    room = session.get('chat_uid')
    join_room(room)
    emit('wtext', {'msg': message['msg']}, room=room)


if __name__ == '__main__':
    #app.run(port=5000, debug=True)
    socketio.run(app, debug=True, port=5000)
