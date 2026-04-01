import math as mt
import os
from sys import exit

def ler_valor(mensagem, tipo = float):
    while(True):
        try:
            valor = input(mensagem)
            return tipo(valor)
        except ValueError:
            print(f"Erro: '{valor}' não é um número válido. Tente novamente.")

def ex1():
    os.system("cls")
    print("EXERCICIO 2.1\n\n")
    a = ler_valor("informe o valor de a: ", int)
    c= ler_valor("informe valor de c: ", int)
    y = a + 151
    b = c * (144+y)
    x = y + (a * b /c)
    print(f"x = {x}")




def ex2():
    """2.2. Peça ao usuário que digite quatro notas bimestrais, calcule e mostre sua média aritmética."""
    os.system("cls")
    print("EXERCICIO 2.2\n\n")
    notas = []
    for i in range(1, 5):

        nota = ler_valor(f"Nota {i}: ")

        notas.append(nota)

    media = sum(notas) / len(notas)

    print(f"A média das notas é: {media}")




def ex3():
    """2.3. Converta um valor digitado em metros para centímetros e exiba o resultado."""
    print("EXERCICIO 2.3\n\n")
    os.system("cls")

    meters = ler_valor("Insira o tamanho em metros: ")
    centimeter = meters * 100
    print(f"{meters} metros são {centimeter} centimetros.\n")



def ex4():
    """ 2.4. Peça o raio de um círculo, calcule e mostre sua área. """
    os.system("cls")
    print("EXERCICIO 2.4\n\n")

    pi = mt.pi
    raio = ler_valor("Insira o raio do circulo: ")
    area_circulo =  pi * (raio ** 2)
    print(f"A area do circulo é: {area_circulo}.\n")



def ex5():
    """"
    2.5. Pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
        Calcule e mostre o total do seu salário no referido mês.
    """
    os.system("cls")
    print("EXERCICIO 2.5\n\n")


    ganho = ler_valor("Quanto você ganha por hora?: ")
    trabalho = ler_valor("Quantas horas você trabalha por dia: ")
    ganho_mensal = ganho*trabalho*30
    print(f"Você ganha, aproximadamente {ganho_mensal} p/mês.\n")




def ex6():
    """
     2.6. Peça ao usuário que digite dois números inteiros e um número real. Calcule e mostre:
     o produto do dobro do primeiro com metade do segundo.2x*n/2
     a soma do triplo do primeiro com o terceiro.
     o terceiro elevado ao cubo.
     """
    os.system("cls")
    print("EXERCICIO 2.6\n\n")


    num1 = ler_valor("Insira um numero inteiro: ", int)
    num2 = ler_valor("Insira outro numero inteiro: ", int)
    num3 = ler_valor("Inisira um numero real: ")
    req1 = num1 *  num2                        # 2*num1*num2/2 = num1 * num2 * (2 / 2) = num1*num2
    req2 = 3 * num1 + num3
    req3 = num3 ** 3

    print("o produto do dobro do primeiro com metade do segundo: ", req1)
    print("\na soma do triplo do primeiro com o terceiro: ", req2)
    print("\no terceiro elevado ao cubo: ", req3)




def ex7():
    """
    2.7. Tendo como dados de entrada a altura (h) de uma pessoa do gênero feminino, construa um
    programa que calcule seu peso ideal, utilizando a seguinte fórmula: (62.1 x h) - 44.7
    """
    os.system("cls")
    print("EXERCICIO 2.7\n\n")


    altura = ler_valor("Insira sua altura em metros: ")
    ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal pra sua altura({altura}m) é: {ideal}\n")




def ex8():

    """
    2.8. Leia dois números inteiros, calcule e exiba a soma dos valores, a subtração do primeiro
    valor do segundo, a multiplicação dos dois,
    o resultado da divisão real entre eles, o
    resultado da divisão inteira entre eles, o valor do primeiro elevado ao segundo e o resto da
    divisão desse cálculo anterior pelo segundo valor digitado.
    """

    os.system("cls")
    print("EXERCICIO 2.8\n\n")


    val1 = ler_valor("Insira um numero inteiro: ")
    val2 = ler_valor("Insira um segundo numero inteiro: ", int)
    pot = val1 ** val2
    print(f"Soma = {val1 + val2}\n")
    print(f"Diferença: {val1 - val2}\n")
    print(f"Divisão real: {val1 / val2}\n")
    print(f"Divisão inteira: {val1 // val2}\n")
    print(f"Primeiro elevado ao segundo: {pot}\n")
    print(f"Resto da potência anterior pelo segundo valor digitado: {pot % val2}\n")




def ex9():
        """2.9. Uma loja de tintas deseja um programa que peça o tamanho em metros quadrados de uma
        área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
        quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
        usuário a quantidades de latas de tinta a serem compradas e o preço total.
        """
        os.system("cls")
        print("EXERCICIO 2.9\n\n")

        
        area = ler_valor("Insira a area da parede em metros quadrados: ")  # 1l = 3m²
        
        litros = area/3   

        caixas = mt.ceil(litros/18)
        custo = caixas * 80.00
        
        print(f"Serão necessarias {caixas} latas de tinta, com o preço total de {round(custo, 2)}R$.\n")
        if custo > 10**7:
            print("é pouco caro")




def main():
    
    escolha =ler_valor("Insira qualquer numero. Insira [0] para ver os enunciados: ", int)
    if escolha == 0 :
        os.system("cls")
        questoes = open('Problemas.txt', 'r', encoding = 'utf-8')
        print(questoes.read())
        ch = ler_valor("a casa decimal do arquivo equivale ao numero do exercicio, deseja continuar? [Y/N]", str)
        if ch[0] == "Y" or ch[0] == "y":
            os.system('cls')
            main()
        elif ch[0] == 'N' or ch[0] == 'n':
            os.system('cls')

    else:

        os.system('cls')

        exn = ler_valor("Escolha o exercicio que deseja verificar de 1 a 9  ", int)
        match exn:
            case 1: ex1()
            case 2: ex2()
            case 3: ex3()
            case 4: ex4()
            case 5: ex5()
            case 6: ex6()
            case 7: ex7()
            case 8: ex8()
            case 9: ex9()
            case _: print("Indice inexistente...\n")




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuario...\n")
        exit(0)