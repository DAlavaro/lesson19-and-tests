# Напишите декоратор called, 
# который при вызове функции будет перед 
# вызовом функции выводить в консоль "функция вызвана"


# TODO напишите декратор called здесь


# Ниже следует код для самопроверки:
# TODO Вы можете попробовать задекорировать функцию func
# в теле которой ничего не происходит.

from flask import request, abort, Flask
from flask_restx import Api, Resource

def called(x):
    def wrapper():
        print('функция вызвана')

    return wrapper

@called
def func():
    pass


if __name__=="__main__":
    func()