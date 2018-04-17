from random import randint
from threading import Thread
from time import sleep

import fake_useragent as ua
import requests

from config import list_tokens, message, method


def main(file_name: str, token: str) -> None:
    with open(file_name, 'r', encoding='UTF8') as file:
        for user_id in file:
            try:
                # Отпровляем сообщния
                res = requests.get(url=method, params={
                    'user_id': user_id.replace('\n', ''),
                    'v': 5.73,
                    'message': message,
                    'access_token': token
                    }, headers={'User-Agent': ua.UserAgent().random})

                print(res.status_code)
                print(f'сообщение отправлено пользователю: https://vk.com/id{user_id}\n'
                      f'С токена {token}')

            except Exception as e:
                print(f'Ошибка: {e}')
                continue

            # Ожидаем
            sleep(randint(30, 100))


if __name__ == '__main__':
    file = 'file\\file{}.txt'
    pool = []
    counter = 1
    for token in list_tokens:
        th = Thread(target=main, args=(file.format(counter), token))
        th.start()
        counter += 1
        pool.append(th)

    for thread in pool:
        thread.join()
