import sys
import re


def predec(wieght:int | float, t0:float | int, t1:float | int) -> int:
    return ((wieght * t1) + t0)

def get_type(value):
    if re.fullmatch(r"\d+", value):  # Matches integers (optional negative sign)
        return int(value)
    elif re.fullmatch(r"\d*\.\d+", value):  # Matches floats (optional negative sign)
        return float(value)
    else:
        print('Please enter a number!')
        sys.exit(1)

def main():
    
    print('Welcome to CPP (Car Price Predictor :)')
    value = input("> Please entre your mileage: ")
    value  = get_type(value)
    

    tetas = open('tetas.txt', "r")
    s = tetas.read()
    s = s.split('\n')
    tetas.close()

    predected = predec(value, float(s[0]), float(s[1]))
    print(f"The estimated price is : {round(predected)}")
    #tetas.close()
    #tetas = open('tetas.txt', "w")
    #tetas.write(str((float(s[0]) + 12)) + '\n' + str((float(s[1]) + 13)))
    #tetas.close()


    #tetas = open('tetas.txt', "r")
    #print(tetas.read())

    #print(tetas.read())

if __name__ == "__main__":
    main()