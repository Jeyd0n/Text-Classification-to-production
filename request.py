import requests


def send_request(request: str):
    """
    Тестовые запросы к API с помощью бибилотеки requests
    """
    response = requests.post(
        'http://127.0.0.1:8000/get_prediction',
        params={
            'request': request
        }
    ).text

    return response


def main():
    texts = [
        'чел говорит на каком то языке фактов, гений фэшн контента во всем мире',
        'как всегда,спасибо за контент',
        'Продолжай пожалуйста, ты мне нужен',
        'как найти песню на фоне? шазам не помогает, очень нравится такая музыка',
        'Я просто зашёл в найк в Риге, купил себе шорты, футболку, кросы, носки и збс. Пошел жить для себя, тренироваться в зале',
        'До слез, не понимаю как можно не любить соус карри',
        'Трогательно. До глубины. До слёз и вдохновения.',
        '',
        '        ',
        'See you again',
        'I really like your new t-shirt',
        'I appreciate how you treat my dauther but you should to be more calm'
    ]

    for idx, text in enumerate(texts):
        print(
            f"Текст под номер {idx + 1} классифицируется как: {send_request(request=text)}"
        )


if __name__ == '__main__':
    main()
