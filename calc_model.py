from input_model import k_num
from input_model import operation

def calc_ration(a, b):
    if '+' in operation:
        result = a + b
        print(f'Результат сложения равен: {result}')
    if '-' in operation:
        result = a - b
        print(f'Результат вычитания равен: {result}')
    if '*' in operation:
        result = a * b
        print(f'Результат умножения равен: {result}')
    if '/' in operation:
        result = a / b
        print(f'Результат деления равен: {result}')
    global res
    res = result
    return res

def calc_complex(c, d):
    if '+' in operation:
        result1 = complex(c + d)
        print(f'Результат сложения равен: {result1}')
    if '-' in operation:
        result1 = complex(c - d)
        print(f'Результат вычитания равен: {result1}')
    if '*' in operation:
        result1 = complex(c * d)
        print(f'Результат умножения равен: {result1}')
    if '/' in operation:
        result1 = complex(c / d)
        print(f'Результат деления равен: {result1}')
    global res1
    res1 = result1
    return res1

def choose_calc(k_num):
    if k_num == 1:
        # from input_model import operation
        from input_model import a, b
        calc_ration(a, b)
    elif k_num == 2:
        # from input_model import operation
        from input_model import c, d
        calc_complex(c, d)

choose_calc(k_num)

