from flask import Flask, render_template, redirect, url_for, request, session, abort
#from .session_interface import MySessionInterface

app = Flask(__name__)
'''app.secret_key = b"?123sxrc3__"
app.session_interface = MySessionInterface()'''


def get_current_username():
    username = ""
    login_auth = False
    if "username" in session:
        username = session["username"]
        login_auth = True
    return username, login_auth


@app.route("/")
def Index():
    username, login_auth = get_current_username()
    return render_template("index.html", username=username, login_auth=login_auth)


@app.route("/contactlist")
def ContactList():
    username, login_auth = get_current_username()
    contactList = [
        ["Berk", "Satış", "Yüksek"],
        ["Ezgi", "İnsan Kaynakları", "Orta"],
        ["Ali", "Nakliye", "Yüksek"],
        ["Ecem", "Üretim", "Düşük"]
    ]
    return render_template("contact_list.html", contactList=contactList, username=username, login_auth=login_auth)


@app.route("/contact", methods=["GET", "POST"])
def Contact():
    username, login_auth = get_current_username()
    if request.method == 'POST':
        pass
    return render_template("contact.html", username=username, login_auth=login_auth)\



@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == 'POST':
        if request.form:
            if "username" in request.form and "password" == request.form:
                username = request.form["username"]
                password = request.form["password"]
                if username == "admin" and password == "admin":
                    #sessions["username"] = username
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
            abort(400)
    username, login_auth = get_current_username()
    return render_template("login.html", username=username, login_auth=login_auth)

@app.route("/logout")
def Logout():
    if "username" in session:
        del session["username"]
    return redirect(url_for("Index"))
