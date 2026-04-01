from eq_prim_grau  import equacao
c = ("\x1b[2J\x1b[1;1H")
def main():
    
    print(c)
    a = float(input(    "Digite o valor do coeficiente linear: "))
    b = float(input("Digite o valor do termo independente: "))
    eq = equacao(a, b)
    eq.solucao()
    
    print(eq)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(c)
        print("Programa interrompido pelo usuario...")