FROM python:3.9

WORKDIR /nlp_app
COPY requirements.txt nlp_app/requirements.txt

RUN pip install --upgrade -r nlp_app/requirements.txt

COPY . /nlp_app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]