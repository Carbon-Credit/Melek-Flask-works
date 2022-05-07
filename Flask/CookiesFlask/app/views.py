from flask import Flask, render_template, redirect, url_for, request, make_response
from  itsdangerous import Signer, BadSignature #cookie için
app = Flask(__name__)


@app.route("/")
def Definition():
    signer = Signer("secret key")
    signed_name = request.cookies.get('name')

    try:
        name = signer.unsign(signed_name).decode()
        print('name', name)
    except:
        print("Bad signature")
    signed_name = signer.sign('Melek')
    response = make_response("<html><body><h1>İlk flask denemeleri</h1></body></html>")
    response.set_cookie('name', signed_name )
    return response


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

