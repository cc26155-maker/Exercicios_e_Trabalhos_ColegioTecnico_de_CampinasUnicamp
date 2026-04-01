class Somatorio:


    def __init__(self):
        self._sum = 0.0             #Resultado da soma
        self._parcel = 0            #Parcelas somadas


    def somar(self, adict : float) -> float:
        self._parcel+=1     #Contador pe incrementado
        self._sum += adict  #Resultado da soma é somado á nova parcela


    @property
    def sum(self):
        return self._sum
    

    @property
    def parcels(self):
        return self._parcel