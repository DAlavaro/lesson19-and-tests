# У вас есть словарь, который содержит 
# данные о пользователе. На его основе 
# сгенерируйте токен. 
#
# В качестве секрета используйте слово 's3cR$eT',
# В качестве алгоритма формирования токена используйте 'HS256'.
# Сгенерированный токен запишите в переменную access_token.
import calendar
import datetime
import jwt

secret = 's3cR$eT'
algo = 'HS256'

data = {
        "username": "Skypro",
        "role": "admin"
        }

def generate_token(data):
        return jwt.encode(data, secret, algorithm=algo)


access_token = generate_token(data)

