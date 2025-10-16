from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Este app está rodando em um container Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
