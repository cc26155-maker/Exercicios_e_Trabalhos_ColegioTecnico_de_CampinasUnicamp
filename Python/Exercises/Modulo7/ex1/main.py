from somatorio import Somatorio
import sys


def main():
    def exercicios():
        def ex1():
            total = Somatorio()
            numero = -1
            qnt = 0
            while numero != 0:
                numero = float(input("Digite o numero a ser somado([0] Para parar a execução): "))
                if numero != 0:
                    total.calcular(numero)
                    qnt +=1
                else: 
                    break
            if qnt > 0:
                print(f"A soma dos termos resulta em: {total.valor}")
                print(f"Média aritmética: {total.valor/total.somados}")
                print(f"Quantidade de termos: {total.somados}")
            else:
                sys.exit(0)

        def ex2():
            qunt = 0
            numero = -1
            total = Somatorio()
            ask = int(input("Quantos numeros inteiros serão somados: "))
            for i in range(1, ask+1):
                total.calcular(i)
                print(i)

            print(f"Soma: {total.valor}")
            print(f"Média aritmética: {total.somados}")
    


if __name__ == "__main__":
    main()