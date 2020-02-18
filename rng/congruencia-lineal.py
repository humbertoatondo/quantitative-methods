
def congruencia_lineal(s, a, c, m):
    xn = s
    for _ in range(30):
        res = a * xn + c
        resMod = res % m
        print("%-8s %-8s %-8s" % (xn, res, resMod))
        xn = resMod

def main():
    print("Ingrese el valor para la semilla, a, c, m separados por un espacio.")
    s, a, c, m = map(int, input().split())
    congruencia_lineal(s, a, c, m)

if __name__ == "__main__":
    main()
