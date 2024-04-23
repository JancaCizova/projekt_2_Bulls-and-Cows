print("projekt_2.py: druhý projekt do Engeto Online Python Akademie")
print("author: Jana Čížová")
print("email: janca.cizova@seznam.cz")
print("discord: Janča Č. - janca_15997")

import random

def vygeneruj_tajne_cislo():
    cislice = list('123456789')
    random.shuffle(cislice)
    tajne_cislo = ''.join(cislice[:4])
    if tajne_cislo[0] == '0':
        tajne_cislo = tajne_cislo[1:] + tajne_cislo[0]
    return tajne_cislo

def ziskej_tip():
    while True:
        tip = input("Zadejte číslo:\n")
        if len(tip) != 4 or not tip.isdigit() or len(set(tip)) != 4 or tip[0] == '0':
            print("Neplatný vstup. Zadejte prosím čtyřmístné číslo s unikátními číslicemi, které nezačíná nulou.")
        else:
            return tip

def vyhodnot_tip(tajne_cislo, tip):
    bulls = sum(a == b for a, b in zip(tajne_cislo, tip))
    cows = sum(a in tajne_cislo for a in tip) - bulls
    return bulls, cows

def main():
    print("Ahoj!")
    print("-----------------------------------------------")
    print("Vygeneroval jsem pro tebe náhodné čtyřmístné číslo.")
    print("Hrajeme hru bulls a cows.")
    print("-----------------------------------------------")

    tajne_cislo = vygeneruj_tajne_cislo()
    pokusy = 0

    while True:
        tip = ziskej_tip()
        pokusy += 1
        bulls, cows = vyhodnot_tip(tajne_cislo, tip)
        if bulls == 4:
            print(f"Správně, uhodl(a) jste správné číslo na {pokusy} pokusů!")
            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
            print("-----------------------------------------------")

    if pokusy <= 4:
        hodnoceni = "úžasný"
    elif pokusy <= 7:
        hodnoceni = "průměrný"
    else:
        hodnoceni = "ne tak dobrý"
    print(f"To je {hodnoceni}!")

if __name__ == "__main__":
    main()
