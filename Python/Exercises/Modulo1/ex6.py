import os

def main():
    """
     2.6. Peça ao usuário que digite dois números inteiros e um número real. Calcule e mostre:
     o produto do dobro do primeiro com metade do segundo.2x*n/2
     a soma do triplo do primeiro com o terceiro.
     o terceiro elevado ao cubo.
     """
    os.system("cls")
    print("EXERCICIO 2.6\n\n")


    num1 = int(input("Insira um inteiro: "))
    num2 = int(input("Insira outro numero inteiro: "))
    num3 = float(input("Insira um numero Real: "))
    req1 = num1 *  num2 # 2*num1 * num2/ 2 = num1*num2/2 = num1*num2
    req2 = 3 * num1 + num3
    req3 = num3 ** 3

    print("o produto do dobro do primeiro com metade do segundo: ", req1)
    print("\na soma do triplo do primeiro com o terceiro: ", req2)
    print("\no terceiro elevado ao cubo: ", req3)






if __name__ == '__main__': main()