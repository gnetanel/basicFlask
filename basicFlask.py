from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")

@app.route("/<users>")
def index(users=None):
    requestMethod = request.method
    if users == None:
        return "Home"
    else:
        return jsonify({'response':'this is the response', 'method': requestMethod})

@app.route("/profile/")
@app.route("/profile/<name>")
def profile(name=None):
    return render_template("profile.html", name=name)


@app.route("/dummy", methods=['GET', 'POST'])
def dummy():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

if __name__ == "__main__":
    app.run()
