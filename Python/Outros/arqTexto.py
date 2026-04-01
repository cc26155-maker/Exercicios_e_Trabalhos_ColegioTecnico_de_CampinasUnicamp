from tkinter import filedialog

def criacao():
    arquivo = open("c:\\temp\\teste.txt","w") # "w" --> write, escrita, saída 
    linha = "xxxxx"
    while linha != "":
        linha = input("Digite um texto para gravar no arquivo ([Enter] sai): ")
        if linha != "":     # usuário digitou texto não vazio
            arquivo.write(linha+"\n")

    arquivo.close() # obrigatório, para gravar todos os dados escritos

def processamento():
    abriu_arquivo = True # supomos inicialmente que o arquivo será aberto

    tiposDeArquivos = ( 
                        ('Arquivos de texto', '*.TXT'), 
                        ('Arquivos JSON',     '*.json'), 
                        ('Qualquer arquivo',  '*.*') 
                      )
    nome_arquivo = filedialog.askopenfilename(
                                title = 'Selecione o arquivo com o poema', 
                                initialdir = r"c:\temp", 
                                multiple = False, 
                                filetypes = tiposDeArquivos)
    
    # nome_arquivo = input("Qual o nome (completo) do arquivo?")
    # r antes da string com o nome do arquivo evita que tenhamos de usar
    # \\ para ignorar os caracteres de escape
    try:
    #     arquivo = open(r"c:\temp\teste.txt", "r")   # "r" --> read, leitura, entrada
        arquivo = open(nome_arquivo, "r")
    except:
        print("Arquivo não encontrado!")
        abriu_arquivo = False   # indica que arquivo não foi aberto

    if abriu_arquivo:
        quantas_linhas = 0
        quantos_caracteres = 0
        quantas_vogais = 0
        quantas_consoantes = 0
        linha = "xxxxx"
        while linha != "":
            linha = arquivo.readline()
            if linha != "":
                if linha != "\n":
                    linha = linha.replace('\n', '')
                print(linha)
                quantas_linhas += 1     # uma nova linha é contada
                quantos_caracteres += len(linha)    # acumula qtde de caracteres
                for caracter in linha:  # percorre caracter a caracter da linha
                    if caracter.upper() >= "A" and caracter.upper() <= "Z":
                        if caracter in "AEIOUaeiou":
                            quantas_vogais += 1
                        else:
                            quantas_consoantes += 1
        
        arquivo.close()
        print(f"Quantas linhas    : {quantas_linhas}")
        print(f"Quantos caracteres: {quantos_caracteres}")
        print(f"Quantas vogais    : {quantas_vogais}")
        print(f"Quantas consoantes: {quantas_consoantes}")

    input("Tecle [Enter] para terminar:")

if __name__ == "__main__":
    # criacao()
    processamento()