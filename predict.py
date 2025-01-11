import sys
import re
from tools import predec,get_theta


def get_type(value):
    if re.fullmatch(r"\d+", value):
        return int(value)
    elif re.fullmatch(r"\d*\.\d+", value):
        return float(value)
    else:
        print('Please enter a number!')
        sys.exit(1)

def main():
    
    print('Welcome to CPP')
    value = input("> Please entre your mileage: ")
    value  = get_type(value)
    
    theta = get_theta()
    predected = predec(value, theta[0], theta[1])
    if predected < 200:
        print("\033[31mWarning: The mileage is outside the training range. The prediction may not be reliable.\033[0m")
    print(f"The estimated price is : {max(round(predected), 0)}")

if __name__ == "__main__":
    main()