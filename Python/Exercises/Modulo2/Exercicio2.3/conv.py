from math import sqrt

class Triangle:
    def __init__(self) -> None:
        self.cat_1  = 0.0
        self.cat_2 = 0.0
        self.hipotenusa = 0.0
        self.perimetro = 0.0
        self.area = 0.0
        self.alpha = 0.0
        self.beta = 0.0
        
    def calcular(self) -> None:
        self.hipotenusa = sqrt(self.cat_1**2 + self.cat_2**2)
        self.perimetro = self.cat_1 + self.cat_2 + self.hipotenusa
        self.area = (self.cat_1 + self.cat_2) / 2
        
        
    def receber_valores(self) -> None:
        self.cat_1 = float(input("Primeiro cateto: "))
        self.cat_2 = float(input("Segundo cateto: "))

        
    def __str__(self):
        return(f"\nDados os catetos a = {self.cat_1} e b = {self.cat_2}, sua hipotenusa  c é {self.hipotenusa}, onde {self.cat_1}²+{self.cat_2}² = {self.hipotenusa}²\n")
