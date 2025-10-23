from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/api")
def Dados():
    return{"nome": "Joao", "idade": 30}

@app.get("/api/{nome}")
def nome(nome:str):
    return {"mensagem": f"seja bem vindo {nome}"}
@app.post("/produto/cadastrar")

def cadastrar(nome: str, idade: int):
    return {"mensage": f"nome: {nome} e idade {idade} cadastrados com sucesso"}


