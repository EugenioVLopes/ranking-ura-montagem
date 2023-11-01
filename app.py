from flask import Flask, render_template

# Importando rotas
from routes.entidade.competidores import competidores_routes

#CORS
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'myawesomesecretkey'

CORS(app,
    origins=["http://127.0.0.1:5500"],
    allow_headers=["Authorization", "Content-Type"],
    supports_credentials=True
    )

@app.route("/")
def login():
    return render_template("index.html")
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

# Registrar as blueprints (rotas) no app
app.register_blueprint(competidores_routes)

if __name__ == "__main__":
    app.run(debug=True, port=3000)