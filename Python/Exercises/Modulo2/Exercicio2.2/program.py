import subprocess
import conv
import sys


def ler():
    subprocess.run('cls', shell = True)
    
    global umcon 
    umcon = conv.Circulo()
    umcon.ler_raio()
    umcon.calc()
    print(umcon)
    
def calcular():
    ...

def main():
    ler()

if __name__ == '__main__':    
    try:
        main()
    except KeyboardInterrupt, ValueError:
        sys.stderr.write("\r\033[K\nPrograma interrompido pelo usuario e\ou erro de inserção de valores.\n")
        sys.exit(1)