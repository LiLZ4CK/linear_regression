import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from predict import predec
from train import calculate_cost
from tools import predec, calculate_mse, grad_desc, get_theta




def main():
    data = pd.read_csv('./data.csv')
    data1 = pd.read_csv('./data.csv')
    data['km'] = data['km'] / 10000
    data['price'] = data['price'] / 10000
    
    t0 = 0
    t1 = 0
    rate = 0.001
    costs = []

    for i in range(100000):
        t0_g, t1_g = grad_desc(data, rate, t0, t1)
        cost = calculate_cost(data1, t0, t1)
        costs.append(cost)
        if i %10000 == 0:
            print(f"cost =={calculate_cost(data, t0, t1)} t0 = {t0_g} t1 = {t1_g}")
        t0 = t0_g
        t1 = t1_g
    t0 *= 10000     
    
    print(f' leen ==== {len(data1)}')
    for i in range(len(data1)):
        print(f"{data1['price'][i]} == {predec(data1['km'][i], t0, t1)}")
        data1['price'][i] = predec(data1['km'][i], t0, t1)
    print(f"{calculate_cost(data1, t0, t1)}")
    data = pd.read_csv('./data.csv')
    sns.regplot(data=data1, x='km', y='price',line_kws={'color': 'red', 'linewidth': 3})
    sns.regplot(data=data, x='km', y='price',line_kws={'color': 'blue', 'linewidth': 1})
    plt.title('data')
    plt.show()
    print('rererererere')

if __name__ == "__main__":
    main()
