import sys
import pandas as pd
from predict import predec
from tools import predec, get_theta, isthere


def ssr_counter(data):
    ssr = 0
    for i in range(len(data)):
        x = data['predec'][i]
        y = data['price'][i]
        ssr += (y - x) ** 2
    return ssr

def tss_counter(data):
    tss = 0
    mean = data['price'].sum() / len(data)
    for i in range(len(data)):
        y = data['price'][i]
        tss += (y - mean) ** 2
    return tss

def main():
    isthere("./data.csv'")
    data = pd.read_csv('./data.csv')
    theta = get_theta()
    data['predec'] = round(predec(data['km'], theta[0], theta[1]))
    ssr = ssr_counter(data)
    tss = tss_counter(data)
    pres = 1 - (ssr / tss)
    if pres < 0:
        pres = 0
    print(f' Precision of your program is {(round(pres, 4) * 100)}%')

if __name__ == "__main__":
    main()

