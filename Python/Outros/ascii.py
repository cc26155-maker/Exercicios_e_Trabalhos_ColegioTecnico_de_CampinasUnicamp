import os
def tabelaASCII() :
 os.system('cls') or None
 print("\n ", end="")
 for codigo in range(0, 16, 1) : # Faz cabeçalho superior
    print(f"{codigo:3d}", end=" ")
 for codigo in range(32, 255) :
    if codigo % 16 == 0 :
        print(f"\n{(codigo):3d} ", end="")
    print(f" {chr(codigo)}", end="")
    tecla: str = input("\n\nPressione [Enter]")
if __name__ == '__main__':
 tabelaASCII()