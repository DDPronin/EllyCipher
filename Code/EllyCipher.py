from decimal import *
import sys
codes = {'0': '10', '1': '11', '2': '12', '3': '13', '4': '14',
         '5': '15', '6': '16', '7': '17', '8': '18', '9': '19',
         ' ': '20', '.': '21', '!': '22', '?': '23', ',': '24',
         'А': '25', 'Б': '26', 'В': '27', 'Г': '28', 'Д': '29',
         'Е': '30', 'Ё': '31', 'Ж': '32', 'З': '33', 'И': '34',
         'Й': '35', 'К': '36', 'Л': '37', 'М': '38', 'Н': '39',
         'О': '40', 'П': '41', 'Р': '42', 'С': '43', 'Т': '44',
         'У': '45', 'Ф': '46', 'Х': '47', 'Ц': '48', 'Ч': '49',
         'Ш': '50', 'Щ': '51', 'Ъ': '52', 'Ы': '53', 'Ь': '54',
         'Э': '55', 'Ю': '56', 'Я': '57', '+': '58', '-': '59',
         '=': '60', '(': '61', ')': '62', '': '63', '': '64',
         '': '65', '': '66', '': '67', '': '68', '': '69',
         '': '70', '': '71', '': '72', '': '73', '': '74',
         '': '75', '': '76', '': '77', '': '78', '': '79',
         '': '80', '': '81', '': '82', '': '83', '': '84',
         '': '85', '': '86', '': '87', '': '88', '': '89',
         '': '90', '': '91', '': '92', '': '93', '': '94',
         '': '95', '': '96', '': '97', '': '98', '': '99'}

d = 100*100

def mode():
    print('+++ Чтобы зашифровать текст введите "1", чтобы расшифровать введите "2" +++')
    m = int(input())
    while m not in (1,2):
        print('Дана некорректная команда! Пожалуйста, повторите запрос.')
        m = int(input())
    if m in (1, 2):
        return m

def encode(data):
    print('Введите ключ шифровки:')
    EllyKey = float(input())
    s = ''
    length = len(data)
    getcontext().prec = 1000
    result = Decimal(EllyKey).ln() * (1 - Decimal(EllyKey).ln())
    for i in range(d, length + d):
        result = result*(1-result)
        #print(result)
        encoded = str(str(result).find(codes[str(data[i-d])]))
        s = s + encoded + '.'
    s = s[:len(s)-1]
    print('Ваше сообщение зашифровано:', s)

def decode(data):
    print('Введите ключ дешифровки:')
    EllyKey = float(input())
    s = ''
    k = 0
    revCodes = {v: k for k, v in codes.items()}
    data = data.split('.')
    length = len(data)
    getcontext().prec = 1000
    result = Decimal(EllyKey).ln() * (1 - Decimal(EllyKey).ln())
    for i in range(d, length + d):
        result = result * (1 - result)
        #print(result)
        try:
            decoded = revCodes[str(str(result)[int(data[i-d])]) + str(str(result)[int(data[i-d])+1])]
            s = s + decoded
            #print('Ваше сообщение расшифровано:', s)
        except BaseException:
            k = 1
    if k == 1:
        print('Введенный вами ключ дешифровки неверен!')
    else:
        print('Ваше сообщение расшифровано:', s)

l = 1
while l == 1:
    choise = mode()
    if choise == 1:
        print('Введите ваше сообщение:')
        m = str(input())
        encode(m)
        print('Если хотите продолжить, введите "1", чтобы завершить работу программы, введите "0"')
        l = int(input())
    if choise == 2:
        print('Введите ваше сообщение:')
        m = str(input())
        decode(m)
        print('Если хотите продолжить, введите "1", чтобы закончить работу, введите "0"')
        l = int(input())



