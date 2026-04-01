import os
import math as mt
def main():
    """ 2.4. Peça o raio de um círculo, calcule e mostre sua área. """
    os.system("cls")
    print("EXERCICIO 2.4\n\n")

    pi = mt.pi
    raio = float(input("insira o raio do circulo: "))
    area_circulo =  pi * (raio ** 2)
    print(f"A area do circulo é, aproximadamente: {round(area_circulo, 2)}\n")


if __name__ == '__main__':
    main()