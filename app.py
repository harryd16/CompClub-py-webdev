from flask import Flask,render_template

app = Flask(__name__)


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

