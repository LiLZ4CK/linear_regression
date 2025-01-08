import sys
import re
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def predec(wieght, t0, t1):
    return wieght * t1 + t0
# 1/2m * E (y - y')
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

def calculate_cost(data, t0, t1):
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

def show_graph(t0, t1, data1, close):
    pred_price = (t0) + t1 * data1['km']
    plt.scatter(data1['km'], data1['price'], color='blue', alpha=0.5, label='Data Points')
    plt.plot(data1['km'],   pred_price, color='red', label='Regression Line')
    plt.title('Car Price vs Mileage')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.legend()
    if(close):
        plt.pause(0.01)
        plt.clf()
    else:
        plt.show()


def get_min(data) ->int:
    x = 10
    i = 0
    while(data > 1):
        x = 10
        data = data / x
        i+=1
    return x ** i

def main():
    print('Welecome to the trainer programe.')
    print('Please wait for the predict programe to be trained!')
    flag = 0
    if(len(sys.argv) == 2):
        flag = sys.argv[1]
        if(flag.isnumeric()):
            flag = int(flag)
        else:
            flag = 0
    data = pd.read_csv('./data.csv')
    data1 = pd.read_csv('./data.csv')
    devided = get_min(min(data['km']))
    data['km'] = data['km'] / devided
    data['price'] = data['price'] / devided
    
    tetas = open('tetas.txt', "r")
    s = tetas.read()
    s = s.split('\n')
    tetas.close()

    t0 = float(s[0])
    t1 = float(s[1])
    rate = 0.001
    print(f'cost1 == {calculate_cost(data1, t0, t1)}')
    s = ''
    add = '█'
    pe = None
    spaces = ' '
    #t0_l = t0
    #t1_l = t1

    t0 = t0 / devided
    ran = range(45000)
    for i in ran:

        t0_g, t1_g = grad_desc(data, rate, t0, t1)
        t0 = t0_g
        t1 = t1_g
        
        p = (i / ran.stop) * 103
        fixed = f"{p:,.0f}"
        km_line = np.linspace(data1['km'].min(), data1['km'].max(), 100)

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
            if(flag > 1):
                show_graph(t0 * devided,t1,data1,1)

    t0 *= devided
    #t0
    print("100%|", s, spaces * (100 - int(fixed)), '| ', i + 1, '/',
          ran.stop, ' [00:01<00:00, 194.13it/s]', sep='', end="\r")
    tetas = open('tetas.txt', "w")
    tetas.write(str(t0) + '\n' + str(t1))
    tetas.close()
    print('\nDone!')
    print(f'cost2 == {calculate_cost(data1, t0, t1)}')
    if (flag > 0):
        show_graph(t0,t1,data1,0)


if __name__ == "__main__":
    main()