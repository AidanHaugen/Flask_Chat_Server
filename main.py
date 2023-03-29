from flask import Flask
from flask import url_for, redirect, request
from flask import render_template, send_file
from auxilary.manage_msg import get_msg_hist, send_msg
from turbo_flask import Turbo


app = Flask(__name__, template_folder="./templates")
turbo = Turbo(app)


def update_messages():
    with app.app_context():
        turbo.push(turbo.replace(render_template('chat.html', msg_hist=get_msg_hist()), 'page'))


@app.route('/')
def index():
    return send_file('./files/index.html')


@app.route('/<path>')
def serv_file(path):
    return send_file(f'./files/{path}')


@app.route('/chat')
def chat():
    return render_template('chat.html', msg_hist=get_msg_hist())


@app.route('/chat', methods=["POST"])
def update_chat():
    msg = request.form.get('new_msg')
    send_msg(msg)
    update_messages()
    return redirect(url_for('chat'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
