from flask import Flask, render_template, redirect, url_for, request, session
from .session_interface import MySessionInterface

app = Flask(__name__)
app.secret_key = b"?123sxrc3__"
app.session_interface = MySessionInterface()


@app.route("/")
def Definition():
    if 'name' in session:
        print('name', session['name'])
    session['name'] = 'Melek'
    session['lastname'] = 'Naz'
    session['username'] = 'MelekNaz'
    return "<html><body><h1>İlk flask denemeleri</h1></body></html>"


@app.route("/hello")
def Hello():
    return render_template("hello.html")


@app.route("/hello-admin")
def HelloAdmin():
    return render_template("hello_admin.html")


@app.route("/hello-user/<name>")
def HelloUser(name):
    if name.lower() == "admin":
        return redirect(url_for(("HelloAdmin")))
    return render_template("hello_user.html", username=name)


'''@app.route("/add/<int:number1>/<int:number2>")
def Add(number1, number2):
    calculation_result = number1 + number2
    return render_template("add.html", number1=number1, number2=number2, result=calculation_result)@app.route("/add/<int:number1>/<int:number2>")
    #tarayıcıya: /add/12/12 yazarak işlemi yaparız
    '''

@app.route("/add")
def Add():
    number1 = int(request.args["number1"])
    number2 = int(request.args["number2"])
    calculation_result = number1 + number2
    return render_template("add.html", number1=number1, number2=number2, result=calculation_result)
    #tarayıcıya: /add?number1=12&number2=12 yazarak işlemi yaparız

@app.route("/login", methods=['POST', 'GET'])
def Login():
    if request.method == 'POST':
        username = request.form["username"]
        return redirect(url_for("HelloUser", name=username))
    else:
        return render_template("login.html")


@app.route("/student")
def Student():
    return render_template("student.html")


@app.route("/result", methods=['POST'])
def Result():
    ContexData = {
        'name': request.form["name"],
        'fizik': request.form["fizik"],
        'mat': request.form["mat"],
        'kimya': request.form["kimya"],
    }
    return render_template("student_result.html", **ContexData)

    '''name = request.form["name"]
    fizik = request.form["fizik"]
    mat = request.form["mat"]
    kimya = request.form["kimya"]
    return render_template("student_result.html", name=name,
                           fizik=fizik,
                           mat=mat,
                           kimya=kimya)'''

