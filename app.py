import os 
import sys
import logging
from dotenv import load_dotenv

from fastapi import FastAPI
from src.models.load_model import load_model


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


load_dotenv()

app = FastAPI()
model = load_model(os.getenv('MODELNAME'))


@app.post('/')
def get_predict(request):
    """
    End-point классифицирует текст, переданный пользователем 
    """

    logger.info('Пользователь сделал запрос к сервису')
    logger.info('Обработка запроса...')

    resonse = model(request)

    logger.info('Запрос успешно обработан')

    return resonse
