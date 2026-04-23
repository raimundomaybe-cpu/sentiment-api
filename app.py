from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API online"}

@app.get("/analisar")
def analisar(texto: str):
    analise = TextBlob(texto)
    polaridade = analise.sentiment.polarity

    if polaridade > 0:
        sentimento = "POSITIVO"
    elif polaridade < 0:
        sentimento = "NEGATIVO"
    else:
        sentimento = "NEUTRO"

    return {"sentimento": sentimento}
