from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    usuario = {
        "nome": "Ana",
        "email": "ana@email.com"
    }

    alunos = ["Carlos", "Maria", "João"]

    return render_template(
        "index.html",
        nome="Janaina",
        idade=20,
        usuario=usuario,
        alunos=alunos,
        nota=8
    )

app.run(debug=True)