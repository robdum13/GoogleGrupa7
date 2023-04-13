x= input('>')

try:
    x=int(x)
    print('a value is:', a)
except ValueError as e:
    print('Eroare de valoare', e)
except NameError as e:
    print('Eroare la declarare', e)
else:
    print('Else')
finally::
    print('Finally')
