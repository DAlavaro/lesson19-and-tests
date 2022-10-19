# Напишите декоратор jsonwrap, 
# который при вызове функции будет 
# результат выполнения функции превращать 
# в json строку и возвращать эту строку. 
# Примем на веру, что данные всегда или словарь или список.
import json

from flask import jsonify


# TODO напишите декратор jsonwrap здесь


# Ниже следует код для самопроверки:
# TODO Вы можете попробовать задекорировать функцию func
# которая возвращает словарь.

def jsonwrap(x):
    def wrapper():
        r = x()
        return json.dumps(r)
    return wrapper

def func():
    return {'text': 'tasks',
            'author': 'skypro'}

if __name__=="__main__":
    func()