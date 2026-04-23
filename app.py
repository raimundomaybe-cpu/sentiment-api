from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis",
                      model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.get("/")
def home():
    return {"status": "API online"}

@app.get("/analisar")
def analisar(texto: str):
    resultado = classifier(texto)[0]["label"]

    if "1" in resultado or "2" in resultado:
        sentimento = "NEGATIVO"
    elif "3" in resultado:
        sentimento = "NEUTRO"
    else:
        sentimento = "POSITIVO"

    return {"sentimento": sentimento}
