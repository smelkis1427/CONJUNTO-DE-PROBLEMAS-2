# Funcion suma elementos en una lista.

from typing import List

def sumlist(numlist: List[int]) -> int:
    suma = 0
    for i in numlist:
        suma = suma + i
    return suma

def main():
    print(sumlist([9, 4, 6, 2, 8, 3]))


if __name__ == 'main':
    main()