import os

def main():
    """
    2.7. Tendo como dados de entrada a altura (h) de uma pessoa do gênero feminino, construa um
    programa que calcule seu peso ideal, utilizando a seguinte fórmula: (62.1 x h) - 44.7
    """
    os.system("cls")
    print("EXERCICIO 2.7\n\n")


    altura = float(input("Insira sua altura em metros: "))
    ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal pra sua altura({altura}m) é: {ideal}\n")




if __name__ == '__main__':
    main()