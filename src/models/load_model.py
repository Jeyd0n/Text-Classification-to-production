import sys
import logging

import transformers
from transformers import pipeline


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_model(modelname: str) -> transformers.pipelines.text_classification.TextClassificationPipeline:
    """
    Фукнция возвращает объект предобученной модели, который нужно использовать для загрузки в app.py
    """
    
    model = pipeline(model=modelname)

    return model
