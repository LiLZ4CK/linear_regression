import sys
import re
from pathlib import Path

def predec(wieght:int | float, t0:float, t1:float) -> int:
    return (wieght * t1) + t0

def grad_desc(data, rate, t0, t1):
    l = len(data)
    sav_t0 = 0
    sav_t1 = 0
    for i in range(l):
        x = data['km'][i]
        y = data['price'][i]
        error = predec(x, t0, t1)
        sav_t0 += error - y
        sav_t1 += (error - y) * x
    t0 -= (rate * 1/l) * sav_t0
    t1 -= (rate * 1/l) * sav_t1
    return t0, t1

def calculate_mse(data, t0, t1):
    total_cost = 0
    m = len(data)
    
    for i in range(m):
        x = data['km'][i]
        y = data['price'][i]
        prediction = predec(x, t0, t1)
        error = prediction - y
        total_cost += error ** 2
    
    mse = total_cost / (2 * m)
    return mse

def is_int_or_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        
def get_theta() ->list[float]:
    my_file = Path("tetas.txt")
    if not my_file.exists():
        print('Cant find tetas')
        sys.exit(1)
    tetas = open('tetas.txt', "r")
    s = tetas.read()
    tetas.close()    
    s = s.split('\n')

    if ((len(s) != 2) or (not is_int_or_float(s[0]) or not is_int_or_float(s[1]))):
        tetas = open('tetas.txt', "w")
        tetas.write(str(0) + '\n' + str(0))
        tetas.close()
        print('Something wrong with prediction program try to learn again')
        sys.exit(1)
    
    return [float(s[0]),float(s[1])]