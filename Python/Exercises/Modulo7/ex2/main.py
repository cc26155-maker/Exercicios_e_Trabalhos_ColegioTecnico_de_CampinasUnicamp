import somatorio


def main():
            qunt = 0
            numero = -1
            total = somatorio.Somatorio()
            ask = int(input("Quantos numeros inteiros serão somados: "))
            for i in range(1, ask+1):
                print(i)
            soma = (ask*(ask+1))/2
            print(f"Soma: {soma}")
            print(f"Média aritmética: {soma / ask}")
if __name__ == "__main__":
        main()