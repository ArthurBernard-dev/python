from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    nome_usuario = "Arthur"
    idade_usuario = 17

    usuario_dict = {
        "nome": "Ana", 
        "email": "ana@email.com"
    }

    lista_alunos = ["Bruno", "Camila", "Daniel", "Elena"]

    nota_final = 7.5

    return render_template(
        'index.html', 
        nome=nome_usuario,
        idade=idade_usuario,
        usuario=usuario_dict,
        alunos=lista_alunos,
        nota=nota_final
    )

if __name__ == '__main__':
    app.run(debug=True)
