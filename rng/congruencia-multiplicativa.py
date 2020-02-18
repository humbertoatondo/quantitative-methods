
def congruencia_multiplicativa(s, a, m):
    xn = s
    for _ in range(30):
        res = (a * xn)
        resMod = res % m
        print("%-8s %-8s %-8s" % (xn, res, resMod))
        xn = resMod

def main():
    print("Ingrese el valor para la semilla, a, m separados por un espacio.")
    s, a, m = map(int, input().split())
    congruencia_multiplicativa(s, a, m)


if __name__ == "__main__":
    main()
