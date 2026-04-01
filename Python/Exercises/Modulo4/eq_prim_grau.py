class equacao:
    def __init__(self, a, b): #constructor
        self._a = a
        self._b =b
        
    def ler_dados(self):
        self._a = float(input("Digite o valor do coeficiente linear: "))
        self._b = float(input("Digite o valor do termo independente: "))
        
        
    def solucao(self):
        
        return (-self._b) / self._a  if  self._a != 0 else None
    
    

    def __str__(self):
        x = (f"X = {self.solucao()}") if self._a != 0 else ("Erro: Divisão por 0...")
        return x
    
