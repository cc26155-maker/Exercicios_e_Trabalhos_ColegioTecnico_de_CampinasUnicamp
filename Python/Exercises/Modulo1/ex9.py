import os
import math as mt
import sys
def main():
    """2.9. Uma loja de tintas deseja um programa que peça o tamanho em metros quadrados de uma
        área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
        quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
        usuário a quantidades de latas de tinta a serem compradas e o preço total.
        """
    os.system("cls")
    print("EXERCICIO 2.9\n\n")

    try:
        area = float(input("Tamanho em metros quadrados da area a ser pintada: "))  # 1l = 3m²
    except ValueError:
        print("Erro: Digite um valor valido.\n")
        sys.exit(0)
        
    litros = area/3   
    if litros < 18:
        caixas = litros / 18
        
    else:
        caixas = int(litros) //18
        
        
        
    caixas = mt.ceil(caixas)
    custo = caixas * 80.00
    
    print(f"Serão necessarias {caixas} latas de tinta, com o preço total de {round(custo, 2)}R$.\n")
    if custo > 10**7:
        print("é pouco caro...")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuario.\n")
        