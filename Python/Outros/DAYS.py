import os


def saud():
    
    print("olá pessoal")
    name = input("Seu nome: ")
    print(f"Bom dia, {name}!")
    
    
def days( nasc, month, day, acty, actm, actd):
    
    bissexto = (abs(nasc - acty))//4
    return (abs((nasc - acty)*365)+  abs(month*30 - actm*30) + (abs(day - actd) + bissexto))


def months(nasc, acty, month, actm):
    return (abs((nasc - acty)*12)+  abs(month - actm))


def years(nasc, month, day, acty, actm, actd):
    dias = days(nasc, month, day, acty, actm, actd)
    return dias//365
    
    
def main():
    
    os.system("cls") or None
    
    saud()
    
    nasc = int(input("Em que ano você nasceu?: "))
    month = int(input("Em que mês?: "))
    day = int(input("Qual dia?: "))
    
    actual_year = int(input("Qual o ano atual da execução deste programa?: "))
    actual_month = int(input("Qual o Mês atual(1-12) da execução deste comando?: "))
    actual_day = int(input("Qual o dia atual da execução deste programa?"))
    
    total_days = days(nasc, month, day, actual_year, actual_month, actual_day)   
    total_months = months(nasc, actual_year, month, actual_month)
    age = years(nasc, month, day, actual_year, actual_month, actual_day)
    
    print(f"Você tem aproximadamente: {total_days}  Dias; {total_months} Meses e  {age} Anos de idade")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo Usuario\n\n")