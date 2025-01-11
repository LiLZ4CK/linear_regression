import sys
import re
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import time as tm
from tools import isthere, grad_desc, get_theta




def show_graph(t0, t1, data1, close):
    km_values = data1['km'].to_numpy()
    pred_price = t0 + t1 * km_values
    plt.scatter(data1['km'], data1['price'], color='blue', alpha=0.5, label='Data Points')
    plt.plot(km_values,   pred_price, color='red', label='Regression Line')
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
    isthere("./data.csv")
    print('Welcome to the training programe.')
    print('Please wait for the prediction programe to be trained:\n')
    flag = 0
    if(len(sys.argv) == 2):
        flag = sys.argv[1]
        if(flag.isnumeric()):
            flag = int(flag)
        else:
            flag = 0
    data = pd.read_csv('./data.csv')
    data1 = pd.read_csv('./data.csv')
    devided = round(get_min(min(data['km'])))
    data['km'] = data['km'] / devided
    data['price'] = data['price'] / devided
    
    theta = get_theta()

    t0 = float(theta[0])
    t1 = float(theta[1])
    rate = 0.001
    s = ''
    add = '█'
    pe = None
    spaces = ' '
    t0 /= devided

    ran = range(65000)
    for i in ran:

        t0_g, t1_g = grad_desc(data, rate, t0, t1)
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
            if(flag > 1):
                show_graph(t0 * devided, t1, data1, 1)

    t0 *= devided
    print("100%|", s, spaces * (100 - int(fixed)), '| ', i + 1, '/',
          ran.stop, ' [00:01<00:00, 194.13it/s]', sep='', end="\r")
    tetas = open('tetas.txt', "w")
    tetas.write(str(round(t0, 3)) + '\n' + str(round(t1, 3)))
    tetas.close()
    print('\n\nDone!')
    if (flag > 0):
        show_graph(t0,t1,data1,0)


if __name__ == "__main__":
    main()