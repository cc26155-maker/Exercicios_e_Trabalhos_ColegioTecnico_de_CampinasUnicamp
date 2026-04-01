import somat

def main():
    ask = int(input("Quantos valores: "))
    numero = -1
    numeros = []
    for i in range(1, ask+1):
        #intervalos:(-infinito, 0), [0, 25], [26,50], 
            #[51,75], [76,100] e (100, +infinito)

        numero = float(input("Insira um numero: "))
        numeros.append(numero)

    for numero in numeros:
        if numero<0:
            print(f"{numero:}:\tIntervalo: (-infinito, 0)")
        elif 0<=numero<=25:
            print(f"{numero}:\tIntervalo: [0, 25]\n")
        elif 26<=numero<=50:
            print(f"{numero}:\tIntervalo: [26, 50]\n")
        elif 51<=numero<=75:
            print(f"{numero}:\tIntervalo: [51, 75]\n")
        elif 76<=numero<=100:
            print(f"{numero}:\tIntervalo: [76,100]\n")
        else:
            print(f"{numero}:\tIntervalo: (100, +infinito)\n")


if __name__ == "__main__":
    main()