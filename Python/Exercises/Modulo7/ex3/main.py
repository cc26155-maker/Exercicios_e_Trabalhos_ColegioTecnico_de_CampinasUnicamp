from prod import Produtorio

def main():
            qunt = 0
            numero = -1
            total = Produtorio()
            ask = int(input("Quantos numeros inteiros serão multiplcados: "))


            for i in range(1, ask+1):
                total.calcular(i)
                print(i)

            print(f"Produto: {total.valor180}")
            print(f"Média Geométrica: {total.valor**(1/ask)}")




if __name__ == "__main__":
    main()