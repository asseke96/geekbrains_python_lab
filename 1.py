'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,а указать явно, в программе.
'''

massiv = ['Hello World!',2,3.14,[['h','l'],(2,3)]]
for elem in massiv:
    print(type(elem))

