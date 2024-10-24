import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



def predec(wieght, t0, t1):
    return wieght * t1 + t0

def cost_calc(data, t0, t1):
    l = len(data)
    total = 0
    for i in range(l):
        x = data['km'][i]
        y = data['price'][i]
        total += ((predec(x, t0, t1) - y) ** 2)
    return (total/(l * 2))

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



def main():
    data = pd.read_csv('./data.csv')
    data1 = pd.read_csv('./data.csv')
    data['km'] = data['km'] / 10000
    data['price'] = data['price'] / 10000
    print(data)
    print("###########################")
    print(data1)
    t0 = 0
    t1 = 0
    rate = 0.001
    costs = []

    for i in range(100000):
        t0_g, t1_g = grad_des(data, rate, t0, t1)
        cost = cost_calc(data1, t0, t1)
        costs.append(cost)
        if i %10000 == 0:
            print(f"cost =={cost_calc(data, t0, t1)} t0 = {t0_g} t1 = {t1_g}")
        t0 = t0_g
        t1 = t1_g
    t0 *= 10000

    for i in range(len(data1)):
        print(f"{data1['price'][i]} == {predec(data1['km'][i], t0, t1)}")
        data1['price'][i] = predec(data1['km'][i], t0, t1)
    print(f"{cost_calc(data1, t0, t1)}")
    data = pd.read_csv('./data.csv')
    sns.regplot(data=data1, x='km', y='price',line_kws={'color': 'red', 'linewidth': 3})
    sns.regplot(data=data, x='km', y='price',line_kws={'color': 'blue', 'linewidth': 1})
    plt.title('data')
    plt.show()
    print('rererererere')

if __name__ == "__main__":
    main()
