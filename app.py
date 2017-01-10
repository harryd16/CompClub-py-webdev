from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_required, login_user, current_user
import flask_login as login

import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data.sqlite')
# This sould be kept secret - probably no as written here
app.config['SECRET_KEY'] = '12345678'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/poll/<int:poll_id>")
def show_poll(poll_id):
    poll = {
        "id" : str(poll_id),
        "title" : "POLL TITLE HERE",
        "description" : "This is a description of poll " + str(poll_id),
        "question" : "This is a question. What do you prefer?"
    }

    return render_template("poll.html", poll=poll)


@app.route("/profile/<username>")
def show_profile(username):
    user = {
        "id" : 1,
        "username" : username,
        "password" : "password"
    }
    return render_template("profile.html", user=user)


if __name__ == "__main__":
    app.run()

