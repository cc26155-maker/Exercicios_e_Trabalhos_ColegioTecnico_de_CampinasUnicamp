from somat import Somatoria
from tkinter import filedialog

def contar():
    valor_final = int(input("Valor final: "))
    contador = 0                        # valor inicial do contador
    while contador < valor_final:       # definir critério de parada
        contador = contador + 2         # contador += 2  incremento
        print(contador,'\t', end="")    # comando feito dentro da contagem

    print()

def medias():
    quantos_alunos = int(input("Quantas médias você vai digitar? "))
    
    contador = 1
    while contador <= quantos_alunos:
        media = float(input(f"Digite a {contador}ª média: "))
        if media >= 5:
            print("Aprovado(a)")
        else:
            print("Retido(a)")
        
        contador = contador + 1   # incrementa o contador          

    print("\nSituações finais dos alunos foram exibidas.")

def somatoria():
    arquivo = open("dadosFunc.txt")         # abre um arquivo para leitura
    print("\nMatr.\tNome\t  Salário")
    totalSalarios = 0.00                    # zera a somatória
    quantos_funcionarios = 0                # contador de funcionários
    dadosLidos = "----"                     # diferente de ""
    while dadosLidos != "":     # diferente de cadeia vazia
        dadosLidos = arquivo.readline()     # lê próxima linha do arquivo
        
        if dadosLidos != "":                # se não acabou o arquivo
            # gera uma lista com os campos separados por ";"
            campos = dadosLidos.split(";")        
            matricula = campos[0]       # primeira posição da lista
            nome = campos[1]            # segunda posição da lista
            salario = float(campos[2])  # terceira posição da lista
            print(f"{matricula}\t{nome}\t{salario:10.2f}")
            totalSalarios = totalSalarios + salario         # somatória
            quantos_funcionarios = quantos_funcionarios + 1 # contagem
    
    arquivo.close()
    media_salarial = totalSalarios / quantos_funcionarios
    print(f"\nA soma dos salários é {totalSalarios:.2f}")
    print(f"A média salarial é {media_salarial:.2f}\n")

def produtorio():
    quantos_valores = int(input("Informe quantos valores digitará: "))
    produtorio = 1
    somatoria = 0
    contador = 1                            # valor inicial da contagem
    while contador <= quantos_valores:      # condição de continuação do while
        um_valor = int(input(f"{contador}º valor: "))   # lê o dado digitado
        somatoria = somatoria + um_valor                # acumula esse dado na soma
        produtorio = produtorio * um_valor              # acumula esse dado no produto

        contador = contador + 1     # incrementa contador para ler próximo valor

    print(f"Soma dos valores digitados   : {somatoria}")
    print(f"Produto dos valores digitados: {produtorio}")


def somar_salarios():
    arquivo = open("dadosFunc.txt", "r", encoding='utf-8')         # abre um arquivo para leitura
    item = processamento()
    pagina  = open(item)

    pagina.write("<html>")

    pagina.write("\n<style>\n table,tr,td{\nborder-collapse:collapse;\n}")
    pagina.write("\nbody{display:flex; justify-content:center; background-color: #f6f6f6; flex-direction: column; padding: 10px;}\n p{color:green;} #error{color:red;}</style>")
    
    pagina.write("\n<body>\n<table border=1>\n")
    
    pagina.write(f"<tr><td>Matricula</td><td>Nome</td><td>Salário</tr>\n")
    # () obrigatório, para chamar __init__() e, assim,
    # instanciar uma instância (objeto) dessa classe
    soma_sal = Somatoria()                  
        
    '''
    try:
        print(soma_sal.media_aritmetica())
    except:
        print("Tentativa de divisão por zero.")
    '''

    dadosLidos = "----"                     # diferente de ""

    while dadosLidos != "":     # diferente de cadeia vazia

        dadosLidos = arquivo.readline()     # lê próxima linha do arquivo

        
        if dadosLidos != "":                # se não acabou o arquivo

            # gera uma lista com os campos separados por ";"
            campos = dadosLidos.split(";")        
            matricula = campos[0]       # primeira posição da lista
            nome = campos[1]            # segunda posição da lista
            try:
                salario = float(campos[2])  # terceira posição da lista
                soma_sal.somar(salario)
                # soma_sal.valor = -12132.00    dará exceção
                pagina.write(f"<tr><td>{matricula}</td><td>{nome}</td><td>{salario:10.2f}</tr>\n")
                
            except Exception as o_erro_que_deu:
                
                print(f"{matricula}\t{nome}\t{campos[2]}\t{o_erro_que_deu}")

    arquivo.close()

    pagina.write("</table>\n")
    
    try:

        pagina.write(f"<p><br>A soma dos salários é {soma_sal.valor:.2f}</p>")
        pagina.write(f"<p><br>A média salarial é {soma_sal.media_aritmetica():.2f}</p>\n")

    except:
        pagina.write("\n<p id = \"error\"><br>Não há dados para média aritmética!</p>")

    pagina.write("</html>")

    pagina.close()
def processamento():
    abriu = True
    tiposDeArquivos =(
        ('Arquivos de Texto', "*.TXT"),
        ('Arquivo JSON', '*.json'),
        ('Qualquer Arquivo', '*.*')

    )
    nomeDoArquivo = filedialog.askopenfilename(title = 'selecione o arquivo',
                                               initialdir = r"c:\temp",
                                               multiple = False,
                                               filetypes = tiposDeArquivos)
    if nomeDoArquivo != "":
        arquivoDeEntrada = open(nomeDoArquivo, "r") 
        ...  
        arquivoDeEntrada.close()

        
if __name__ == "__main__":
   # contar()
   # medias()
   # somatoria()
   # produtorio()
   somar_salarios()
   # print(chr(181))
   
