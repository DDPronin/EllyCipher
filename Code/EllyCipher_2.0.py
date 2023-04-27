from decimal import *
import random


symCodes = {'0': '10', '1': '11', '2': '12', '3': '13', '4': '14',
         '5': '15', '6': '16', '7': '17', '8': '18', '9': '19',
         ' ': '20', '.': '21', '!': '22', '?': '23', ',': '24',
         'А': '25', 'Б': '26', 'В': '27', 'Г': '28', 'Д': '29',
         'Е': '30', 'Ё': '31', 'Ж': '32', 'З': '33', 'И': '34',
         'Й': '35', 'К': '36', 'Л': '37', 'М': '38', 'Н': '39',
         'О': '40', 'П': '41', 'Р': '42', 'С': '43', 'Т': '44',
         'У': '45', 'Ф': '46', 'Х': '47', 'Ц': '48', 'Ч': '49',
         'Ш': '50', 'Щ': '51', 'Ъ': '52', 'Ы': '53', 'Ь': '54',
         'Э': '55', 'Ю': '56', 'Я': '57', '+': '58', '-': '59',
         '=': '60', '(': '61', ')': '62', 'A': '63', 'B': '64',
         'C': '65', 'D': '66', 'E': '67', 'F': '68', 'G': '69',
         'H': '70', 'I': '71', 'J': '72', 'K': '73', 'L': '74',
         'M': '75', 'N': '76', 'O': '77', 'P': '78', 'Q': '79',
         'R': '80', 'S': '81', 'T': '82', 'U': '83', 'V': '84',
         'W': '85', 'X': '86', 'Y': '87', 'Z': '88', '': '89',
         '': '90', '': '91', '': '92', '': '93', '': '94',
         '': '95', '': '96', '': '97', '': '98', '': '99'}


keyCodes = {'A': '10', 'a': '11', 'B': '12', 'b': '13', 'C': '14',
         'c': '15', 'D': '16', 'd': '17', 'E': '18', 'e': '19',
         'F': '20', 'f': '21', 'G': '22', 'g': '23', 'H': '24',
         'h': '25', 'I': '26', 'i': '27', 'J': '28', 'j': '29',
         'K': '30', 'k': '31', 'L': '32', 'l': '33', 'M': '34',
         'm': '35', 'N': '36', 'n': '37', 'O': '38', 'o': '39',
         'P': '40', 'p': '41', 'Q': '42', 'q': '43', 'R': '44',
         'r': '45', 'S': '46', 's': '47', 'T': '48', 't': '49',
         'U': '50', 'u': '51', 'V': '52', 'v': '53', 'W': '54',
         'w': '55', 'X': '56', 'x': '57', 'Y': '58', 'y': '59',
         'Z': '60', 'z': '61', ':': '62', ';': '63', '1': '64',
         '2': '65', '3': '66', '4': '67', '5': '68', '6': '69',
         '7': '70', '8': '71', '9': '72', '0': '73', '/': '74',
         '.': '75', ',': '76', '=': '77', '+': '78', '-': '79',
         '@': '80', '!': '81', '&': '82', '^': '83', '%': '84',
         '~': '85', '>': '86', '<': '87', '*': '88', '|': '89',
         '#': '90', '(': '91', ')': '92', '"': '93', '_': '94',
         '№': '95', '{': '96', '}': '97', '[': '98', ']': '99'}


revSymCodes = {v: k for k, v in symCodes.items()}
revKeyCodes = {v: k for k, v in keyCodes.items()}


depth = 1000


def mode():
    print('+++ Чтобы зашифровать текст введите "1", чтобы расшифровать введите "2", чтобы сгенерировать ключ введите "3" +++')
    m = int(input())
    while m not in (1, 2, 3):
        print('Дана некорректная команда! Пожалуйста, повторите запрос.')
        m = int(input())
    if m in (1, 2, 3):
        return m


def key_generation():
    k = []
    length = input('Введите длину ключа: \n')
    if length.isdigit():
        for i in range(int(length)):
            randinx = random.randint(48, 127)
            k.append(chr(randinx))
        return "::" + ''.join(k) + "::"
    else:
        print('Введена некорректная длина ключа!')
        key_generation()


def encode(data):
    print('Введите ключ шифровки:')
    EllyKey = str(input())[2:-2]
    s = ''
    NumericEllyKey = ''
    for letter in EllyKey:
        NumericEllyKey += keyCodes[letter]
    getcontext().prec = 2000
    EllyFuncFactor = Decimal('-1.42') - Decimal(str(NumericEllyKey)) / (Decimal('10')**(len(NumericEllyKey)+2))
    length = len(data)
    result = 0
    for i in range(depth):
        result = result ** 2 + EllyFuncFactor
    for i in range(length):
        result = result ** 2 + EllyFuncFactor
        #print(result)
        encoded = str(str(result).find(symCodes[str(data[i])]))
        s = s + encoded + '.'
        for j in range(depth):
            result = result ** 2 + EllyFuncFactor
    s = s[:len(s)-1]
    print('Ваше сообщение зашифровано:', s)


def decode(data):
    print('Введите ключ дешифровки:')
    EllyKey = str(input())[2:-2]
    s = ''
    NumericEllyKey = ''
    for letter in EllyKey:
        NumericEllyKey += keyCodes[letter]
    getcontext().prec = 2000
    EllyFuncFactor = Decimal('-1.42') - Decimal(NumericEllyKey) / (Decimal('10')**Decimal((len(NumericEllyKey)+2)))
    k = 0
    data = data.split('.')
    length = len(data)
    #getcontext().prec = 2000
    result = 0
    for i in range(depth):
        result = result ** 2 + EllyFuncFactor
    for i in range(length):
        result = result ** 2 + EllyFuncFactor
        try:
            decoded = revSymCodes[str(str(result)[int(data[i])]) + str(str(result)[int(data[i])+1])]
            s = s + decoded
            for j in range(depth):
                result = result ** 2 + EllyFuncFactor
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
    if choise == 3:
        print(key_generation())