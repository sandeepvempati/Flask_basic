from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Flask"

@app.route('/user')
def user():
    return "<h2>Hi people</h2>"

@app.route('/profile/<username>')
def profile(username):
    return "<h1>Hey there %s</h1>" % username

@app.route('/show/<int:post_id>')
def post(post_id):
    return "post id is %s"%post_id

if __name__ == "__main__":
    app.run(debug=True)