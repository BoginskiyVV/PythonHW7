# kind_num = int(input('Выбор вида чисел 1 - рациональные 2 - комплексные: '))
# print(kind_num)  # 1 or 2
# global k_num
# k_num = kind_num
# operation = list(input('Выбор операции на числами + - / *: '))
# print(operation)

# def input_numbers(kind_num):
#     if kind_num == 1:
#         x = float(input('Введите первое число: '))
#         global a
#         a = x        
#         print(a)
        
#         y = float(input('Введите второе число: '))
#         global b
#         b = y
#         print(y)
#         return x, y

#     else:
#         z1 = complex(input('Введите первое комплексное число: '))
#         global c
#         c = z1
#         print(c)
#         z2 = complex(input('Введите второе комплексное число: '))
#         global d
#         d = z2
#         print(d)
#         return c, d

# input_numbers(kind_num)


def numbers():
    kind_num = int(input('Выбор вида чисел 1 - рациональные 2 - комплексные: '))
    print(kind_num)  # 1 or 2
    global k_num
    k_num = kind_num
    return k_num

def oper():
    oper = list(input('Выбор операции на числами + - / *: '))
    global operation
    operation = oper
    print(operation)
    return operation

def input_numbers(k_num):
    if k_num == 1:
        x = float(input('Введите первое число: '))
        global a
        a = x        
        print(a)
        y = float(input('Введите второе число: '))
        global b
        b = y
        print(y)
        return a, b
    else:
        z1 = complex(input('Введите первое комплексное число: '))
        global c
        c = z1
        print(c)
        z2 = complex(input('Введите второе комплексное число: '))
        global d
        d = z2
        print(d)
        return c, d

numbers()
oper()
input_numbers(k_num)