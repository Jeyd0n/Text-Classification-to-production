import os 
from dotenv import load_dotenv

from fastapi import FastAPI
from src.models.load_model import load_model


load_dotenv()

app = FastAPI()
model = load_model(os.getenv('MODELNAME'))


@app.get('/')
def get_predict(request: str):
    return model(request)
