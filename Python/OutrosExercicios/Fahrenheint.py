
import os


class Converter:
    def __init__(self, celsius):
        self.celsius = celsius
        self.fahrenheit = 0.00
    def conversao(self):
        self.fahrenheit = (9*self.celsius)/5 + 32
        return self.fahrenheit

        
    def __str__(self):

        return(f"{self.celsius}C celsius em fahrenheint são {self.fahrenheit}F.")
    
        
def receive_value(msg, tp = float):
    while(True):
        try:
            return tp(input(msg))
        except ValueError:
            raise ValueError("Erro de inserção...")



def main():
    
    cels = receive_value("Celsius: ", float)
    
    conv = Converter(cels)
    conv.conversao()
    print(conv)

if __name__ == "__main__":

    try:
        main()
        
    except KeyboardInterrupt:
        raise TypeError("\nPrograma interrompido pelo user.\n")