import re


def convert_numbers_under20(x):
    return {
        0: '',
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять',
        10: 'десять',
        11: 'одинадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятьнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать',
    }[x]


def convert_numbers_1_to_99(x):
    if x == 0:
        return ''
    if 0 < x < 20:
        return convert_numbers_under20(x)
    if 20 <= x < 39:
        return convert_numbers_under20(int(x / 10)) + 'дцать ' + convert_numbers_under20(int(x % 10))
    if 40 <= x < 50:
        return 'сорок ' + convert_numbers_under20(int(x % 10))
    if 50 <= x < 90:
        return convert_numbers_under20(int(x / 10)) + 'десят ' + convert_numbers_under20(int(x % 10))
    if 90 <= x < 100:
        return 'девяносто ' + convert_numbers_under20(int(x % 10))


def convert_hundreds(x):
    hundreds = int(x / 100)
    if hundreds == 0:
        return ''
    if hundreds == 1:
        return 'сто '
    if hundreds == 2:
        return 'двести '
    if 2 < hundreds < 5:
        return convert_numbers_under20(hundreds) + 'ста '
    if 5 <= hundreds < 10:
        return convert_numbers_under20(hundreds) + 'сот '


def convert_under_999(x):
    return convert_hundreds(x) + convert_numbers_1_to_99(int(x % 100))


def convert_thousands(x):
    thousands = int(x / 1000)
    if thousands == 0:
        return ''
    if re.match('\d*[^1]1$', str(thousands)) or thousands == 1:
        return convert_under_999(thousands - thousands % 10) + ' одна тысяча '
    if re.match('\d*[^1]2$', str(thousands)) or thousands == 2:
        return convert_under_999(thousands - thousands % 10) + ' две тысячи '
    if re.match('\d*[^1][3,4]$', str(thousands)) or thousands in [3, 4]:
        return convert_under_999(thousands) + ' тысячи '
    if re.match('\d*[5-9|0]$', str(thousands)) or re.match('\d*[1][1-4]$', str(thousands)):
        return convert_under_999(thousands) + ' тысяч '


def number_converter(x):
    if x > 1000000:
        return "не знаю"
    if x == 1000000:
        return 'миллион'
    if 0 < x < 1000000:
        return convert_thousands(x) + convert_under_999(int(x % 1000))
    if x == 0:
        return 'ноль'


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input
            break


print(number_converter(input_number('Give me a number: ')))
