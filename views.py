from flask import Flask, escape, request,request,redirect,render_template
from  member import *

app = Flask(__name__)
app.register_blueprint(member)

@app.route('/')
def Index():
    return "This is Home Page"



if __name__ == '__main__':
    app.run(debug=True)

