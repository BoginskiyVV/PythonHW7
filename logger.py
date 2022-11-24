from datetime import datetime
from input_model import k_num

def log_ration():
    from input_model import operation, a, b
    from calc_model import res
    time = datetime.now().strftime("%d.%m.%Y %H:%M")
    with open('log_result.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{time};{a};{operation};{b}; =; {res};\n'.format())

def log_complex():
    from input_model import operation, c, d
    from calc_model import res1
    time = datetime.now().strftime("%d.%m.%Y %H:%M")
    with open('log_result.csv', 'a', encoding='UTF-8') as file:
        file.write(f'{time};{c};{operation};{d}; =; {res1};\n'.format())

def choose_log(k_num):
    if k_num == 1:
        log_ration()
    elif k_num == 2:
        log_complex()

choose_log(k_num)