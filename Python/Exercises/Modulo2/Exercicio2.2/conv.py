import subprocess


class Circulo:
    def __init__(self):
        self.raio = 0
        self.diametro = 0
        self.area = 0
        self.circ = 0
        
        
        
        
    def ler_raio(self):
        while(True):
            self.raio = float(input("Raio: "))
            if(self.raio <=0 or self.raio is not type(float)):
                
                print("\nRaio não pode ser uma palavra, simbolo, letra ou menor que ou igual a 0.\n")
            else:
                return
        
        
        
        
    def calc(self):
        subprocess.run("cls", shell = True)
    
        self.area = self.raio*self.raio*3.14159
        self.diametro = self.raio*2
        self.circ = self.raio*3.14159*2
        
        
    def __str__(self):
        return(f"\nraio ={self.raio}\narea = {self.area}\ndiametro = {self.diametro}\ncircunferencia = {self.circ}\n\n")
    