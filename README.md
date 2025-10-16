# 🚀 Meu App com Docker e GitHub Actions
---

![Build Status](https://github.com/mariotko9/meu-app-docker/actions/workflows/docker.yml/badge.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Este projeto é um exemplo simples de aplicação Flask empacotada com Docker e integrada com GitHub Actions para build, testes automatizados e integração contínua.

---
## 📚 Índice

- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🐍 Aplicação Flask](#-aplicação-flask)
- [🧪 Testes Automatizados com Pytest](#-testes-automatizados-com-pytest)
- [🐳 Dockerfile](#-dockerfile)
- [🧪 Testar Localmente](#-testar-localmente)
- [☁️ Subir para o GitHub](#️-subir-para-o-github)
- [⚙️ GitHub Actions: Pipeline de Build e Teste](#️-github-actions-pipeline-de-build-e-teste)
- [🧪 Simulações de Erros](#-simulações-de-erros)
- [📣 Badges](#-badges)
- [✅ Resultado](#-resultado)

---
## 📁 Estrutura do Projeto
```
meu-app/<br> 
├── app.py<br>
├── requirements.txt<br>
├── test_app.py<br>
├── Dockerfile<br>
├── .github/<br>
├── workflow/<br>
├── docker.yml
```

## 🐍 Aplicação Flask

**`app.py`**
```
cpython
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Este app está rodando em um container Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
requirements.txt
```
flask==2.3.2
```

🧪 Testes Automatizados com Pytest

test_app.py
```
def test_home():
    from app import app
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Olá, mundo" in response.data
```

🐳 Dockerfile

Dockerfile
```

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt pytest

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

🧪 Testar localmente
```
docker build -t meu-app .
docker run -p 5000:5000 meu-app
```

☁️ Subir para o GitHub
```
git init
git remote add origin https://github.com/SEU_USUARIO/meu-app-docker.git
git add .
git commit -m "Projeto com Docker e Flask"
git branch -M main
git push -u origin main
```

⚙️ GitHub Actions: Pipeline de Build e Teste
```
.github/workflows/docker.yml

name: Build e Teste do Docker

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do código
      uses: actions/checkout@v3

    - name: Configurar Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Build da imagem Docker
      run: docker build -t meu-app .

    - name: Rodar container para teste
      run: docker run -d -p 5000:5000 meu-app

    - name: Testar resposta do app
      run: |
        sleep 5
        curl --fail http://localhost:5000

    - name: Rodar testes com pytest
      run: pytest test_app.py
```
  ✅ Resultado

A cada push ou pull request:

    O GitHub Actions builda a imagem Docker

    Roda o container

    Testa a resposta HTTP

    Executa testes automatizados com pytest

🧪 Simulações de Erros

    ❌ Dependência inexistente no requirements.txt

    ❌ Erro de sintaxe no app.py

    ❌ Porta incorreta no app.run()

    ✅ Testes automatizados com pytest

    
📣 Badges

    Build Status: mostra se o último workflow passou ou falhou

    Docker Ready: indica que o projeto está conteinerizado

    License: exibe o tipo de licença do projeto

Feito com ❤️ usando Docker, Flask e GitHub Actions
