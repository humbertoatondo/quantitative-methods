import matplotlib.pyplot as plt
import random

def genrate_values(n: int = 10000, s: int = 0, e: int = 100000):
    lst = []
    for _ in range(n):
        random_number = random.randint(s, e)
        lst.append(random_number)
    return lst


def main():
    values = genrate_values()
    plt.hist(values, rwidth = 0.9, color = "orange")
    plt.show()

if __name__ == "__main__":
    main()