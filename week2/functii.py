# print("String")
# var1= 1
# print("String {}".format(var1))
# input("Adauga o cifra")
# def functie_adunare(param1):
#     print('print')
#     return param1, '-'
#
# functie_adunare(1)

# def get_sum(a: int, b: int =2,c:int =3, *args) -> (int,int):
#     suma = a+b+c
#     for i in args:
#         suma +=1
#     return suma


def get_sum(a: int, b: int =2,c:int =3, **kwargs) -> (int,int):
    suma = a+b+c
    diferenta = a- b -c
    print(kwargs,type(kwargs))
    for i in kwargs.values():
        suma +=1
        diferenta-=1
    return suma, diferenta
var1, var2= get_sum(1,4, c=-3, d=3,e=4, f=5)
print(var1, var2)