import os

def main():
    os.system("cls")
    print("EXERCICIO 2.1\n\n")

    a = int(input("informe o valor de a: "))
    c= int(input("informe valor de c: "))
    y = a + 151
    b = c * 144+y
    x = y + (a * b )/ c

    print(f"x = {x}")


if __name__ == '__main__':
    main()