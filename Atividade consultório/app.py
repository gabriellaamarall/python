from flask import Flask, render_template, request

app = Flask(__name__)

dados_especialidades = {
    "Cardiologia": [
        {
            "nome": "Dr. André Souza",
            "crm": "CRM/MG 18432",
            "planos": ["Unimed", "Amil", "SulAmérica"]
        },
        {
            "nome": "Dra. Fernanda Melo",
            "crm": "CRM/MG 22105",
            "planos": ["Bradesco Saúde", "Unimed"]
        },
    ],

    "Pediatria": [
        {
            "nome": "Dra. Carla Nunes",
            "crm": "CRM/MG 15780",
            "planos": ["Unimed", "Hapvida", "Amil"]
        },
        {
            "nome": "Dr. Lucas Ribeiro",
            "crm": "CRM/MG 31209",
            "planos": ["SulAmérica", "NotreDame"]
        },
    ],

    "Dermatologia": [
        {
            "nome": "Dra. Juliana Costa",
            "crm": "CRM/MG 29801",
            "planos": ["Amil", "Bradesco Saúde"]
        },
    ],
}


@app.route("/", methods=["GET", "POST"])
def index():

    especialidade = ""
    medicos = []
    erro = ""

    if request.method == "POST":

        especialidade = request.form.get("especialidade", "").strip()

        # Corrige letras maiúsculas/minúsculas
        especialidade = especialidade.title()

        # Campo vazio
        if not especialidade:
            erro = "Digite uma especialidade médica."

        # Busca parcial
        else:
            encontrado = False

            for esp in dados_especialidades:

                if especialidade.lower() in esp.lower():
                    especialidade = esp
                    medicos = dados_especialidades[esp]
                    encontrado = True
                    break

            if not encontrado:
                erro = f'A especialidade "{especialidade}" não está cadastrada.'

    return render_template(
        "index.html",
        especialidade=especialidade,
        medicos=medicos,
        erro=erro,
        total_especialidades=len(dados_especialidades),
        especialidades=dados_especialidades.keys()
    )


if __name__ == "__main__":
    app.run(debug=True)