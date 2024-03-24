import sys

def sumuj(liczba):
    str_liczba = str(liczba)
    n = len(str_liczba)

    iloczyny = [f"{int(str_liczba[i])} * {10 ** (n - i - 1)}" for i in range(n)]

    suma = " + ".join(iloczyny)
    return suma


x = sys.stdin.readline().strip()
x = int(x)
suma = sumuj(x)
sys.stdout.write(f"Podaną liczbę {x} można zapisać jako: {suma}\n")
