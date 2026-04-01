
import os
from sys import exit 

class Converter:
    def __init__(self, celsius):
        self.celsius = celsius
        self.fahrenheit = 0.00
        
    def conversao(self):
        self.fahrenheit = (9*self.celsius)/5 + 32
        return self.fahrenheit
        
    def __str__(self):
        return(f"{self.celsius}C° celsius em fahrenheint são {self.fahrenheit}F°.")
    
        
