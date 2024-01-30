

BLACK='30'
RED='31'
GREEN='32'
YELLOW='33'
BLUE='34'
MAGENTA='35'
CYAN='36'
WHITE='37'

USAGE_BAR_SIZE = 50
USAGE_STATE_DEF = {'IDLE': {'per': (0, 50), 'color': GREEN}, 
                   'ALERT': {'per': (51, 75), 'color': YELLOW},
                   'CRITICAL': {'per': (76, 100), 'color': RED}
                   }

def set_color(color):
    return f"\033[{color}m"

def clear_color():
    return f"\033[0m"

def print_colored(msg, color, end="\n"):
    print(f'{set_color(color)}{msg}{clear_color()}', end=end)

def draw_bar(per):
    char_per_act = '▌'
    char_per_int = '-'
    bar = char_per_int * USAGE_BAR_SIZE
    size=len(bar)
    for i in range(0, size):
        if i<size*(per/100.0):
            bar = bar[:i] + char_per_act + bar[i+1:]
        else:
            bar = bar = bar[:i] + char_per_int + bar[i+1:]
    return f'{bar}'
