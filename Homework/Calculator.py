operatie=input("Alege operatia pe care doresti sa o executi: ")
lista_operatii=['+','-','*','/']
rezultat= 0
def adunare(a,b):
    return a + b
def scadere(a, b):
    return a-b
def impartire(a, b):
    if b != 0:
        return a / b
    else:
        print("Nu se poate efectua împărțirea la 0!")
def inmultire(a, b):
    return a * b
def reset():
    return 0

while True:
    if operatie in lista_operatii:
        if operatie == '+':
            a = float(input("Introduceți primul număr: "))
            b = float(input("Introduceți al doilea număr: "))
            rezultat = adunare(a,b)
            print(f"Suma celor doua numere {a} + {b} = {rezultat} ")
        elif operatie == '-':
            a = float(input("Introduceți primul număr: "))
            b = float(input("Introduceți al doilea număr: "))
            rezultat = scadere(a,b)
            print(f"Diferenta celor doua numere {a} - {b} = {rezultat}")
        elif operatie =='*':
            a = float(input("Introduceți primul număr: "))
            b = float(input("Introduceți al doilea număr: "))
            rezultat = inmultire(a,b)
            print(f"Produsul celor doua numere {a} * {b} = {rezultat}")
        else:
            a = float(input("Introduceți primul număr: "))
            b = float(input("Introduceți al doilea număr: "))
            rezultat = impartire(a,b)
            if rezultat is not None:
                print(f"Impartirea celor doua numere {a} / {b} = {rezultat}")
        break
    elif operatie.lower() == 'c':
        rezultat = reset()
        print("Calculator resetat. Rezultat: ", rezultat)
        break
    else:
        print(f"Alege o operatie din lista: {','.join(['+', '-' , '*', '/','c'])}")
        break