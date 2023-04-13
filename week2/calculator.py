operator_1=input("Primul operator: ")
operator_2=input("Al doilea operator: ")
operatie=input("Alege operatia pe care doresti sa o executi: ")
lista_operatii=['+','-','*','/']
"""introduce litere in loc de cifre"""
"""impartirea la 0"""
while True:
    if operatie in lista_operatii and operator_1.isdigit() and operator_2.isdigit():
        if operatie == '+':
            print(f"Suma celor doua numere {operator_1} + {operator_2}= {int(operator_1) + int(operator_2)}")
        elif operatie == '-':
            print(f"Diferenta celor doua numere {operator_1} - {operator_2}= {int(operator_1) - int(operator_2)}")
        elif operatie =='*':
            print(f"Produsul celor doua numere {operator_1} * {operator_2}= {int(operator_1) * int(operator_2)}")
        else:
            print(f"Impartirea celor doua numere {operator_1} / {operator_2}= {int(operator_1) / int(operator_2)}")
        break
    elif operator_2 == 0 and operatie == '/':
        print (f'Impartirea la 0 nu este permisa')
    else:
        print(f"Alege o operatie din lista: {','.join(['+', '-' , '*', '/'])}")