from conv import Tempo
import subprocess

def main():
    tempo = Tempo()
    tempo.ler_dados()
    tempo.calcular_total()
    tempo.exibir_resultados()


if __name__ == "__main__":
    main()
    