import sys
import re
import pandas as pd


def predec(wieght, t0, t1):
    return wieght * t1 + t0

def grad_des(data, rate, t0, t1):
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

def cost_calc(data, t0, t1):
    l = len(data)
    total = 0
    for i in range(l):
        x = data['km'][i]
        y = data['price'][i]
        total += ((predec(x, t0, t1) - y) ** 2)
    return (total/(l * 2))

def main():
    print('Welecome to the trainer programe.')
    print('Please wait for the predict programe to be trained!')

    
    data = pd.read_csv('./data.csv')
    data1 = pd.read_csv('./data.csv')
    data['km'] = data['km'] / 10000
    data['price'] = data['price'] / 10000
    
    tetas = open('tetas.txt', "r")
    s = tetas.read()
    s = s.split('\n')
    tetas.close()

    t0 = float(s[0])
    t1 = float(s[1])
    rate = 0.001
    costs = []


    s = ''
    add = '█'
    pe = None
    spaces = ' '

    ran = range(100000)
    for i in ran:

        t0_g, t1_g = grad_des(data, rate, t0, t1)
        cost = cost_calc(data1, t0, t1)
        costs.append(cost)
        t0 = t0_g
        t1 = t1_g
        
        p = (i / ran.stop) * 103
        fixed = f"{p:,.0f}"
        if fixed != pe:
            pe = fixed
            z = int(fixed)
            if (int(fixed) > 100):
                fixed = 100
                z += 1
            s += add
            print(end="\r")
            print(fixed, "%|", s, spaces * (103 - z), '| ', i, '/', ran.stop,
                  ' [00:01<00:00, 194.13it/s]', sep='', end="\r")
    t0 *= 10000

    print("100%|", s, spaces * (100 - int(fixed)), '| ', i + 1, '/',
          ran.stop, ' [00:01<00:00, 194.13it/s]', sep='', end="\r")
    tetas = open('tetas.txt', "w")
    tetas.write(str(t0) + '\n' + str(t1))
    tetas.close()
    print('\nDone!')

if __name__ == "__main__":
    main()