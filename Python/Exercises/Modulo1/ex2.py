import os
import sys
def main():

    os.system("cls")
    print("EXERCICIO 2.2\n\n")
    notas = []
    for i in range(1, 6):
        try:
            nota = float(input(f"Nota {i}: "))
        except ValueError:
            print("Entrada invalida, insira apenas numeros...\n ")
            sys.exit(0)
            
        if nota > 10 or nota<0 or type(nota) != float:
            print("Erro de entrada, 0<=nota<=10")
            main()
        else:
            
            notas.append(nota)

    media = sum(notas) / len(notas)

    print(f"A média das notas é: {media:.2f}\n")
if __name__ == '__main__':
    main()