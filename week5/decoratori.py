# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
#
# print(functie_simpla())

def decorator_depozit(material):
    def ambalaj(functia_noastra):
        def ambalaj_intern(*carte):
            return f"Ambalam produse din {functia_noastra__name__} cu {material} care contine cartea "

