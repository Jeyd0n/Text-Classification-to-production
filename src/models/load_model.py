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
    Фукнция возвращает объект предобученной модели, который можно использовать в конечном продукте
    """
    
    model = pipeline(model=modelname)

    return model
