import time
import psutil
from view import *
import subprocess


def display_cpu_usage(cpu_usage):

    cpu_bar = draw_bar(cpu_usage)
    
    if cpu_usage > USAGE_STATE_DEF['IDLE']['per'][1]:
        cpu_state = USAGE_STATE_DEF['ALERT']
    elif cpu_usage > USAGE_STATE_DEF['ALERT']['per'][1]:
        cpu_state = USAGE_STATE_DEF['CRITICAL']
    else:
        cpu_state = USAGE_STATE_DEF['IDLE']
    
    print('\rCPU Usage: ', end="")
    print_colored(cpu_bar, cpu_state['color'], end="")
    print_colored(f'{cpu_usage}%', cpu_state['color'], end="\n")


def display_mem_usage(mem_usage):
    mem_bar = draw_bar(mem_usage)

    if mem_usage > USAGE_STATE_DEF['IDLE']['per'][1]:
        mem_state = USAGE_STATE_DEF['ALERT']
    elif mem_usage > USAGE_STATE_DEF['ALERT']['per'][1]:
        mem_state = USAGE_STATE_DEF['CRITICAL']
    else:
        mem_state = USAGE_STATE_DEF['IDLE']


    print('MEM Usage: ', end="")
    print_colored(mem_bar, mem_state['color'], end="")
    print_colored(f'{mem_usage}%', mem_state['color'], end="\n")





while True:
   
    display_cpu_usage(psutil.cpu_percent())
    display_mem_usage(psutil.virtual_memory().percent)
    time.sleep(0.5)
    subprocess.run(['clear'])
    