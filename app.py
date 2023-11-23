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


@app.get('/')
def main():
    """
    Старовый end-point, на который попадает каждый юзер при переходе на страничку сайт
    """

    logger.info('Пользователь успешно зашел на страницу')
    logger.info('-' * len('Пользователь успешно зашел на страницу'))

    return 'Сервер запущен корректно и работает без ошибок'


@app.post('/get_predict')
def get_predict(request):
    """
    End-point классифицирует текст, переданный пользователем 
    """

    logger.info('Пользователь сделал запрос к сервису')
    logger.info('Обработка запроса')

    logger.info('.')
    logger.info('..')

    resonse = model(request)

    logger.info('...')

    logger.info('Запрос успешно обработан')
    logger.info('-' * len('Пользователь сделал запрос к сервису'))

    return resonse
