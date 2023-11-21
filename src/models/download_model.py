import sys
import logging

from transformers import pipeline


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

modelname = "seara/rubert-tiny2-russian-sentiment"

def download(modelname: str) -> None:
    """
    Данная функция используется для первоначальной загрузки предобученной модели
    для сентемантической классификации русских текстов из репозетория HuggingFace
    """

    logger.info('Начало загрузки предобученной модели из HuggingFace Hub')
    pipeline(model=modelname)
    logger.info('Модель успешно загружена на ваше устройство')


if __name__ == '__main__':
    download(modelname=modelname)
    