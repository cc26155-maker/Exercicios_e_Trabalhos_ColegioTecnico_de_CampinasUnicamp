from flowmeter import Flow
import subprocess 

def ver(num:int):
        if num == 1: return "Crítico: Punitivo (Ansiedade)"
        if num == 2: return "Crítico: Monótono (Tédio)"
        return "Ideal: Zona de Flow"



def analisar_fase(nome_fase):
    print(f"\n--- Coletando dados: {nome_fase} ---")
    dif = float(input(f"Dificuldade {nome_fase}: "))
    rec = float(input(f"Recompensa {nome_fase}: "))
    temp = float(input(f"Duração {nome_fase}: "))
    
  
    f = Flow(dif, rec, temp)
    f.calcular_tudo()
    return f
def metodo_welford(dados):
    n = 0
    media = 0.0
    M2 = 0.0
    
    for x in dados:
        n += 1
        delta = x - media
        media += delta / n
        delta2 = x - media
        M2 += delta * delta2

    if n < 2:
        return {"media": media, "variancia": 0.0, "desvio_padrao": 0.0}

    # Variância amostral (n-1)
    variancia = M2 / (n - 1)
    desvio_padrao = variancia ** 0.5
    
    return {
        "media": media,
        "variancia": variancia,
        "desvio_padrao": desvio_padrao,
        "contagem": n
    }





def fullgame():
    
    fases = {
        "Early": analisar_fase("EarlyGame"),
        "Middle": analisar_fase("MiddleGame"),
        "End": analisar_fase("EndGame")
    }

    print("\n" + "="*40)
    print("      RELATÓRIO COMPLETO DE DESIGN      ")
    print("="*40)
    indiceDeFlowTotal = 0
    tensaoTotal = 0
    engajamentoTotal = 0
    flowajustadoTotal = 0
    statusgeral = ""
    flows = []
    for nome, flow in fases.items():
        print(f"\n>> {nome.upper()}:")
        print(f"   Status:         {flow.status_formatado}")
        print(f"   Índice de Flow: {flow.indiceflow:.2f}")
        print(f"   Tensão:         {flow.tensao:.2f}")
        print(f"   Engajamento:    {flow.engajamento:.2f}")
        print(f"   Flow Ajustado:  {flow.flowajustado:.2f}")
        flows.append(flow.flowajustado)
        if flow.monotono:
            statusgeral+="1"
        if flow.punitivo:
            statusgeral+="2"
        if flow.flowmode:
            statusgeral +="3"
        
        input("PRESSIONE [ENTER] PARA PROSSEGUIR")
        



        indiceDeFlowTotal += flow.indiceflow
        tensaoTotal +=flow.tensao
        engajamentoTotal +=flow.engajamento
        flowajustadoTotal += flow.flowajustado

        print("-" * 20)
    msg = ""
   
    if statusgeral.count("1") >= 2:
        msg = ver(1)
    elif statusgeral.count("2") >= 2:
        msg = ver(2)
    elif statusgeral.count("3") >= 2:
        msg = ver(0) # Ideal
    else:
        msg = "Disperso/Instável"

    metodo_welford(flows)
    print(f"\n>> RELATORIO GERAL(média):")
    print(f"   Status:         {msg}")
    print(f"   Índice de Flow: {indiceDeFlowTotal/3:.2f}")
    print(f"   Tensão:         {tensaoTotal/3:.2f}")
    print(f"   Engajamento:    {engajamentoTotal/3:.2f}")
    print(f"   Flow Ajustado:  {flowajustadoTotal/3:.2f}")
    print(f"Variância Média do Flow ajustado?: {}")
    input("PRESSIONE [ENTER] PARA SAIR")
    return fases

def main():
    
    try:
        limpar_tela()
        
        dificuldade = float(input("O quão dificil/desafiador é o seu jogo: "))
        recompensa = float(input("O quão recompensador é o jogo: "))
        tempo = float(input("Quanto tempo de jogo é minimo para zerar: "))

    except ValueError | ZeroDivisionError  as e:
        print(f"Erro: {e}")

    limpar_tela()
    flow = Flow(dificuldade, recompensa, tempo)
    
    flow.calcular_tudo()
    print("\n" + "="*40)
    print("      RELATÓRIO RÁPIDO DE DESIGN      ")
    print("="*40)
    print(f"\tStatus:            {flow.status_formatado}")
    print(f"\tIndice de Flow:    {flow.indiceflow:.2f}")
    print(f"\tTensão:            {flow.tensao:.2f}")
    print(f"\tEngajamento:       {flow.engajamento:.2f}")
    print(f"\tFlow Ajustado:     {flow.floawajustado:.2f}")
    print("_" * 20)
    input("PRESSIONE [ENTER] PARA SAIR")

def limpar_tela():
    subprocess.run("cls" if subprocess.os.name == "nt" else "clear", shell=True)

def seletor():
    limpar_tela()
    print("=== FLOW METER ANALYZER ===")
    print("[1] Análise Rápida (Geral)")
    print("[2] Análise por Fases (Early/Mid/End)")
    
    escolha = input("\nSelecione uma opção: ")
    
    limpar_tela()
    if escolha == "2":
        fullgame()
    else:
        main()

if __name__ == "__main__":
    seletor()