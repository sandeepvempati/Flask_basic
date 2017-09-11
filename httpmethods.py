from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return "This is %s method" %request.method

@app.route('/bacon',methods=['GET','POST'])
def bacon():
    if request.method == 'POST':
        return "<h1>you are using post</h1>"
    else:
        return "<h1>you are using get</h1>"

if __name__ == "__main__":
    app.run()