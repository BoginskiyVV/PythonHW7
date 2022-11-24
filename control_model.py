from statistics import mode
from input_model import k_num
import input_model as input
import calc_model as calc
import logger as log

def start_calc():
    input.numbers()
    input.oper()
    input.input_numbers(k_num)
    calc.choose_calc(k_num)
    log.choose_log(k_num)

