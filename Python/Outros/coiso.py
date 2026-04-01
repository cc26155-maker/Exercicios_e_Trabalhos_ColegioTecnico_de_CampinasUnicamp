from typing import Callable



class somatorio:
    def __init__(self, inicio, fim, function: Callable[[int], float]):
        self.inicio = inicio
        self.fim = fim
        self.function = function

        
    def calculate(self):
        if self.inicio <= self.fim: return sum(self.function(i) for i in range(self.inicio, self.fim + 1))
        else: return sum(self.function(i) for i in range(self.inicio, self.fim -1, -1))
        
    def __str__(self):
        return print(f"O somatorio de {self.function} para i variando de {self.inicio} até {self.fim} é: {self.calculate()}")
    
def ligar(self):

    pass

def main():
    s1 = somatorio(1, 5, lambda i: i**2)
    print(s1)  # 1² + 2² + 3² + 4² + 5² = 55

def limpar(self):

    subprocess.t=run("cls")



if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        raise TypeError("\nEncerrado pelo Usuario\n")