import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def estimate_price(mileage, t0, t1):
    return t0 + t1 * mileage

def cost_f(data, t0, t1):
    total = 0
    for i in range(len(data)):
        x = data['km'][i]
        y = data['price'][i]
        total += (estimate_price(x, t0, t1) - y) ** 2
    return (total / (2 * len(data)))

def grad_des(data, l_rate, t0, t1):
    m = len(data)
    
    # Calculate gradients
    t0_grad = (1 / m) * sum(estimate_price(data['km'][i], t0, t1) - data['price'][i] for i in range(m))
    t1_grad = (1 / m) * sum((estimate_price(data['km'][i], t0, t1) - data['price'][i]) * data['km'][i] for i in range(m))
    
    # Update t0 and t1
    t0 -= l_rate * t0_grad
    t1 -= l_rate * t1_grad
    
    return t0, t1

def min_max_normalization(data, column):
    min_val = data[column].min()
    max_val = data[column].max()
    data[column] = 1 + ((data[column] - min_val) / (max_val - min_val)) * (100 - 1)



def main():
    km = 'km'
    price = 'price'
    data = pd.read_csv('./data.csv')
    data1 = pd.read_csv('./data.csv')

    min_max_normalization(data, km)
    min_max_normalization(data, price)
    
    l_rate = 0.0001
    t0 = 0
    t1 = 0
    print('test', data1['price'][0])
    total = cost_f(data1, t0, t1)
    print('Initial cost:', total)

    for i in range(1000000):  # Increased iterations to 1000
        t0, t1 = grad_des(data, l_rate, t0, t1)
        if (i % 10000) == 0:  # Print cost every 100 iterations
            print(f"Iteration {i/10000}, Cost: {cost_f(data1, t0, t1)}, t0: {f'{t0:,.4e}'}, t1: {f'{t1:,.4e}'}")
    
    print(f'Final cost: {cost_f(data1, t0, t1)}')
    print(f"Let's try y = mx + b, {data1[price][0]} = {f'{t0:,.4e}'} * {data1[km][0]} + {f'{t1:,.4e}'} = {f'{(t0 * int(data1[km][0]) + t1):,.4e}'}")

if __name__ == "__main__":
    main()
