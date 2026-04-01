from som import Somatorio
from prod import Produtorio
from mdc import Mdc




def main() -> None:
    pass
def seletor():
    
    print("[0] - Terminar o programa")
    print("[1] - Estatística de uma lista de valores lidos de um arquivo texto")
    print("[2] - MMC entre dois valores digitados")
    print("[3] - Raiz Cúbica de um valor digitado")
    print("[4] - MDC por subtrações sucessivas")
    print("[5] - Lista de números de Fibonacci")



def estatisticas():

    ponderal_result = Somatorio()       #soma dos valores com peso
    arithmetical_result = Somatorio()   #soma dos valores sem peso
    ponderals_sum = Somatorio()         #soma dos pesos

    filename = input("Insira o caminho do arquivo(*.txt): ")
    file = open(filename, 'r')
    line = "_____"

    value = 0                          #valor
    ponderosity = 0             #ponderabilidade
    while(line != ""):          #enquanto não houver linhas vazias...

        line = file.readline()
        campo = line.split(";") #cria uma lista com o par (valor;ponderabilidade)
        
        value = campo[0]        #valor
        ponderosity = campo[1]  #peso

        arithmetical_result.somar(value)            #soma  somente os valores 
        ponderal_result.somar(value*ponderosity)    #soma os valores em produto com seus pesos
        ponderals_sum.somar(ponderosity)            #soma somente os pesos
        

        raizMediaQuadrada(arithmetical_result.sum, arithmetical_result.parcels)
        arithmeticalAverage(arithmetical_result.sum, arithmetical_result.parcels)
        geometricAverage(ponderal_result.sum, ponderals_sum)
        



    def raizMediaQuadrada(value : float, parcels : int) -> float:
        rmq = ((1/parcels)*value)**1/2
        return rmq
    

    def arithmeticalAverage(value : float, parcels : int) -> float:
        average = value/parcels
        return average
    
    def geometricAverage(pond_value : float, parcels):
        mg = pond_value ** (1/parcels)
        return mg
    
    





if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Erro: Programa interrompido pelo usuário.")
        