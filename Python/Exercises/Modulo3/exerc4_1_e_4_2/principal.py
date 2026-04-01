import subprocess, os
import temp as t        # as t --> apelido (alias) para o arquivo temp.py
import num4 as n

def seletor_de_opcoes():
    os.system('cls') or None
    print("Opções deste programa:")
    print("0 - Sair do programa")
    print("1 - Exercício 4.1        2 - Exercício 4.2")
    print("3 - logo mais            4 - logo mais")
    print("... tenha paciência que mais exercícios virão!")
    opcao_digitada = int(input("Digite sua opção:"))
    return opcao_digitada

def exercicio_4_1():        # instancia objeto dessa classe
    uma_agua = t.Temp_Agua()
    uma_agua.ler_dados()
    uma_agua.exibir_estado_da_agua()
    input("Pressione [Enter] para retornar ao seletor: ")

def exercicio_4_2():
    um_numero = n.Numero_de_4_Digitos()    # instancia objeto dessa classe
    um_numero.ler_dados()                  # lê o número a ser verificado 
    if um_numero.tem_4_digitos():          # tem 4 dígitos 
        if um_numero.atende_a_propriedade():
            print("Esse número atende a propriedade esperada.")
        else:
            print("Esse número não tende a propriedade esperada.")
    else:                                  # não tem 4 dígitos
        print("\nNúmero não tem 4 dígitos! Impossível verificar.")

    input("Pressione [Enter] para retornar ao seletor: ")
    

def principal():
    opcao = 1   # para ter um valor inicial != 0 e entrar no while na 1a vez
    while opcao != 0:
        opcao = seletor_de_opcoes()
        match opcao:
            case 1 : exercicio_4_1()
            case 2 : exercicio_4_2()

    print("\nPrograma encerrado.\n")

if __name__ == "__main__":
    principal()