from Python.provaA.soma import Somatoria
from Python.provaA.prod import Produtorio

def tratar_arquivo():

    soma = Somatoria()
    produto = Produtorio()
    contador_linhas = 0
    try:
        
        nomeArquivo = input("Nome do arquivo de texto(*.txt) a ser lido: ")
        arquivo = open(nomeArquivo, "r")
        qnt_linhas = arquivo.readline()
        contador_linhas+=1
        linha = "---"
        while linha != "":
            linha = arquivo.readline()

            if linha != "":
                contador_linhas+=1
                soma.somar(float(linha))
                soma.somar_inverso(float(linha))
                produto.multiplicar_ignorando_zero(float(linha))
    
        arquivo.close()

        print(f"Quantidade de valores lidos do arquivo: {qnt_linhas}")
        print(f"Valor da soma dos valores reais lidos do arquivo texto: {soma.valor}")
        print(f"Valor da soma dos inversos dos valores lidos do arquivo texto: {soma.soma_inversos}")
        print(f"valor da media aritmética dos valores lidos no arquivo de texto: {soma.mediaAritmetica()}")
        print(f"Valor da media harmônica dos valores reais lidos do arquivo texto: {soma.media_harmonica}")
        print(f"Maior valor lido: {soma.maximo}")
        print(f"Menor valor lido: {soma.minimo}")
        print(f"Amplitude dos dados: {soma.maximo - soma.minimo}")
        print(f"Valor da variância: {soma._m2}")
        print(f"Media geometrica dos valores multiplicados: {produto.mediaGeometrica()}")
        print(f"Produto normalizado dos valores multiplicados: {produto.produto_normalizado()}")
        print(f"Taxa geométrica média dos valores que foram multiplicados: {produto.taxa_geometrica_media()}")
        
    except Exception as e:
        print(f"Ocorreu um erro na linha {contador_linhas}:", e)

if __name__ == "__main__":
    tratar_arquivo()