from SerieHarm import Harmonica as harm
import subprocess
def main():
    subprocess.run("cls", shell=True)
    ser = harm(1, 10**6)
    
    ser.func()
    print(ser)
 

if __name__ == "__main__":
    main()
