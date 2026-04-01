import os

def main():
    """2.3. Converta um valor digitado em metros para centímetros e exiba o resultado."""
    print("EXERCICIO 2.3\n\n")
    os.system("cls")

    meters = float(input("Insira o valor em metros: "))
    centimeter = meters * 100
    print(f"{meters} metros são {centimeter} centimetros.\n")


if __name__ == '__main__':
    main()