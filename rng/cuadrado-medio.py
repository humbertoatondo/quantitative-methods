
def cuadrado_medio(rn):
    i = 0
    while rn > 1:
        sq = str(rn ** 2)
        size = len(str(rn))
        s = (len(sq) - size) // 2
        res = int(str(sq)[s:s+size])
        print("%-10s %-10s %-10s %-10s" %(i, rn, sq, res))
        rn = res
        i += 1

def main():
    print("Ingrese el valor de rn.")
    rn = int(input())
    cuadrado_medio(rn)

if __name__ == "__main__":
    main()
