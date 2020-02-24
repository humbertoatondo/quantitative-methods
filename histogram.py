import matplotlib.pyplot as plt
import random
import math

def genrate_values_muller(n: int = 10000, s: int = 0, e: int = 100000):
    lst = []
    for _ in range(n):
        random_number = random.randint(s, e)
        random_number2 = random.randint(s, e)
        x1 = normalize(random_number, s, e)
        x2 = normalize(random_number2, s, e)
        x1, x2 = box_muller_transform(x1, x2)
        
        lst.append(x1)
        lst.append(x2)
    return lst


def genrate_values_transform(n: int = 10000, s: int = 0, e: int = 100000):
    lst = []
    for _ in range(n):
        random_number = random.randint(s, e)
        x1 = normalize(random_number, s, e)
        x1 = inverse_transform(x1)
        lst.append(x1)
    return lst

def inverse_transform(x: int):
    try:
        return -math.log(1 - x) / 0.5
    except:
        return 0


def normalize(x: float, s: int, e: int):
    return (x - s) / (e - s)


def box_muller_transform(r1: float, r2: float):
    x1 = 0
    x2 = 0
    try:
        x1 = math.sqrt(-2 * math.log(r1)) * math.cos(2 * math.pi * r2)
        x2 = math.sqrt(-2 * math.log(r1)) * math.sin(2 * math.pi * r2)
    except:
        pass

    return (x1, x2)

def main():
    values = genrate_values_transform()
    values_m = genrate_values_muller()

    plt.hist(values, bins = 69, rwidth = 0.95, color = "orange")
    plt.hist(values_m, bins = 69, rwidth = 0.95, color = "red")
    plt.show()

if __name__ == "__main__":
    main()
