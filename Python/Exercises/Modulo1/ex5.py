import os

def main():
    """"
    2.5. Pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
        Calcule e mostre o total do seu salário no referido mês.
    """
    os.system("cls")
    print("EXERCICIO 2.5\n\n")


    ganho = float(input("Quanto você ganha por hora?: "))
    ganho_mensal = ganho*24*30
    print(f"Você ganha, aproximadamente {ganho_mensal} p/mês.\n")




if __name__ == '__main__':
    main()