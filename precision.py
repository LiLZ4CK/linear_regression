import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from predict import predec
from train import calculate_mse
from tools import predec, calculate_mse, grad_desc, get_theta


def ssr_counter(data):
    ssr = 0
    for i in  range(len(data)):
        x = data['predec'][i]
        y = data['price'][i]
        ssr += (y - x) ** 2
    return ssr

def tss_counter(data):
    tss = 0
    mean = data['price'].sum() / len(data)
    for i in  range(len(data)):
        y = data['price'][i]
        tss += (y - mean) ** 2
    return tss

def main():
    data = pd.read_csv('./data1.csv')
    theta = get_theta()
    data['predec'] = round(predec(data['km'], theta[0], theta[1]))
    ssr = ssr_counter(data)
    tss = tss_counter(data)
    pres = 1 - (ssr / tss)
    print(pres)

if __name__ == "__main__":
    main()
