from flask import Flask, request
app = Flask(__name__, static_folder="")



@app.route("/submit")
def fun1():
    user = request.args.get("username")
    passw = request.args.get("password")
    print(user, passw)
    return "USER REGISTERED SUCCESSFULLY" if passw=="1234" and user=="ankit" else "Wrong password"


@app.route("/")
def index():
    return open("login.html").read()

app.run("0.0.0.0")