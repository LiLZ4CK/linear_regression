import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def predec(wieght, t0, t1):
    return wieght * t1 + t0

def cost_calc(data, t0, t1):
    l = len(data)
    total = 0
    for i in range(l):
        x = data['wei'][i]
        y = data['pri'][i]
        total += ((predec(x, t0, t1) - y) ** 2)
    return (total/(l * 2))

def grad_des(data, rate, t0, t1):
    l = len(data)
    sav_t0 = 0
    sav_t1 = 0
    for i in range(l):
        x = data['wei'][i]
        y = data['pri'][i]
        error = predec(x, t0, t1)
        sav_t0 += error - y
        sav_t1 += (error - y) * x
    t0 -= (rate * 1/l) * sav_t0
    t1 -= (rate * 1/l) * sav_t1
    return t0, t1



def main():
    data = pd.read_csv('./silver.csv')
    t0 = 0
    t1 = 0
    rate = 0.00001
    for i in range(100000):
        t0_g, t1_g = grad_des(data, rate, t0, t1)
        if i %100000 == 0:
            print(f"cost =={cost_calc(data, t0, t1)} t0 = {t0_g} t1 = {t1_g}")
        t0 = t0_g
        t1 = t1_g
    for i in range(len(data)):
        print(f"{data['pri'][i]} == {predec(data['wei'][i], t0, t1)}")
    print(f"{predec(100, t0, t1)}")
    

if __name__ == "__main__":
    main()
