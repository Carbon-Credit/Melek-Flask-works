from flask import Flask, render_template

app = Flask(__name__) 


@app.route("/")
def Definition():
    return "<html><body><h1>İlk flask denemesi</h1></body></html>"


@app.route("/hello")
def Hello():
    return render_template("hello.html")

@app.route("/hello-admin")
def HelloAdmin():
    return render_template("hello_admin.html")

@app.route("/hello-user/<name>")
def HelloUser(name):
    return render_template("hello_user.html", username=name)   