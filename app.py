from fastapi import FastAPI
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API online"}

@app.get("/analisar")
def analisar(texto: str):
    # Traduzir para inglês
    texto_en = GoogleTranslator(source='auto', target='en').translate(texto)

    analise = TextBlob(texto_en)
    polaridade = analise.sentiment.polarity

    if polaridade > 0:
        sentimento = "POSITIVO"
    elif polaridade < 0:
        sentimento = "NEGATIVO"
    else:
        sentimento = "NEUTRO"

    return {"sentimento": sentimento}
