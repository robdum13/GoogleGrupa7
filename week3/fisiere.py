"""
w -> scriem,daca fisierul nu exista,il adauga, daca exista ceva deja scris in fisier,rescrie
a->scriem,daca exista ceva in fisier,il adauga pe urmatorul rand,nu apare eroare daca fisierul nu exista
r+ -> scriere,citire, daca fisierul nu exista, apare eroare
r -> citim,nu adaugam, daca fisierul nu exista apare eroare
"""

file = open('data.txt','r')
# file.write('Hello2')
# file.close()

# try:
#     file.write("hello")
# finally:
#     file.close()

with open('data.txt', 'r') as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line)

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)