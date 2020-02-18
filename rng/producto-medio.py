
def producto_medio(rn, rn1):
    i = 0
    res = 10
    while res > 0:
        mult = str(rn * rn1)
        size = len(str(rn1))
        s = (len(mult) - size) // 2

        while mult[s] == "0":
            s += 1
            if s + size >= len(mult):
                size -= 1
                
        res = int(str(mult)[s:s+size])
        if len(mult) <= 2:
            res = 0
        print("%-10s %-10s %-10s %-10s %-10s" % (i, rn, rn1, mult, res))
        rn = rn1
        rn1 = res
        i += 1

def main():
    print("Ingrese los valores de rn y rn+1 en la misma linea, separados por un espacio.")
    rn, rn1 = map(int, input().split())
    producto_medio(rn, rn1)

if __name__ == "__main__":
    main()
