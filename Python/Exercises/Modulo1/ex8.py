import os
import sys
def main():

    """

    2.8. Leia dois números inteiros, calcule e exiba a soma dos valores, a subtração do primeiro
    valor do segundo, a multiplicação dos dois,
    o resultado da divisão real entre eles, o
    resultado da divisão inteira entre eles, o valor do primeiro elevado ao segundo e o resto da
    divisão desse cálculo anterior pelo segundo valor digitado.

    """
    
    os.system("cls")
    print("EXERCICIO 2.8\n\n")


    val1 = int(input("Insira um numero inteiro: "))
    val2 = int(input("Insira um segundo numero inteiro: "))
    pot = sys.set_int_max_str_digits(val1 ** val2)
    print(f"Soma = {val1 + val2}\n")
    print(f"Diferença: {val1 - val2}\n")
    print(f"Divisão real: {val1 / val2}\n")
    print(f"Divisão inteira: {val1 // val2}\n")
    print(f"Primeiro elevado ao segundo: {pot}\n")
    print(f"Resto da potência anterior pelo segundo valor digitado: {pot % val2}\n")



if __name__ == '__main__':
    main()