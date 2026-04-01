import numpy as np
import sys
def main():
    M = np.array([[1,2,3],
                 [2,3,4]])
    M *= 2
    
    while(True):
        print(M)
        M+=1




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("\r\033[K\nPrograma interrompido pelo usuario.\n")
        sys.exit(1)
