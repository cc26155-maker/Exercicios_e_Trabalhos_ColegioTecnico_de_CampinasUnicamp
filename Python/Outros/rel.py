import time
import subprocess

def contador():

    #relógio
    seg = 0
    h = 0
    min = 0

    #total
    segt = 0
    mint = 0
    hto = 0




    while True:
        
        time.sleep(1)
        subprocess.run("cls", shell = True)

        seg += 1 
        segt += 1
        
        if seg >= 60:
            seg = 0
            min += 1

        if min >= 60:
            min = 0
            h += 1


        if segt % 60 == 0:
            mint += 1

        if mint%60 == 0 and mint != 0:
            hto+=1


        print("\tTempo:", end = " ")

        print(f"{h:02}:{min:02}:{seg:02}\n")

        print(f"\tSegundos totais: {segt:02}\n")

        print(f"\tMinutos totais: {mint:02}\n")

        print(f"\tHoras totais: {hto:02}\n")
        print("\n\n\t Sair: [Ctrl + c]")




def main():
    contador()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ki:
        print("\nPrograma interrompido pelo usuario...\n")
        