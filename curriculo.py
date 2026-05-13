from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    '''
    data = {
        "nome": "ARTHUR BERNARD FERREIRA ANTUNES",
        "telefone": "(31) 98790-0616",
        "email": "aberanrdantunes@gmail.com",
        "escolas": [
            {"instituicao": "Colégio Cotemig", "curso": "Estudante", "ano": "2024 - 2026"}
        ],
        "experiencia": [
            {"cargo": "Desenvolvedor Python Júnior", "empresa": "Tekinisa", "periodo": "Jan 2025 - Atual"}
        ],
        "cursos": [
            "Certificação Python Developer",
            "Workshop de Machine Learning com Flask",
            "Gestão de Projetos Ágeis"
        ],
        "idiomas": {
            "Inglês": "Avançado",
            "Espanhol": "Intermediário"
        }
    }
    return render_template('index.html', resume=data)
   '''

if __name__ == '__main__':
    app.run(debug=True)
