from conv import Converter
import subprocess
import os
from sys import exit

def receive_value(msg, tp = float ):
    erros = 0
    while(True):
        try:
            return tp(input(msg))
        except ValueError:
            os.system("cls") or None
            print("Erro: Valor inserido incorretamente.")
            erros+=1
        if erros>=3:
            os.system("cls") or None
            print("você é idiota?...")
            if erros >= 5:
                os.system("cls") or None
                print("você deve estar brincando...")
                if erros >= 10:
                    os.system("cls") or None
                    print("Isso não é engraçado...")
                    if erros>=15:
                        os.system("cls")
                        print("Irei te ignorar, fds...")
                        if erros>=20:
                            os.system("cls")
                            print("Desisto\n")
                            exit(0)
                    
              
              

               
               
               
                    
                    
                    
def main():

    cels = 0
    os.system("cls")
    cels = receive_value("Celsius([-p]para parar): ")
    conv = Converter(cels)
    conv.conversao()
    print(conv)
    
    
    
if __name__ == "__main__":

    try:
        main()
        
    except KeyboardInterrupt:
        raise TypeError("\nPrograma interrompido pelo user.\n")