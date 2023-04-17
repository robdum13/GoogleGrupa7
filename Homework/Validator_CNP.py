from datetime import datetime
v=0
CNP=input("Please enter CNP: ")

if len(CNP)!=13:
    print("CNP invalid")
    v=1

if not CNP.isdigit():
    print("CNP invalid! Please use only digits!")
    v=1
# We verify S
s= int(str(CNP)[0])
if s not in range(1,9):
    print("S invalid")
    v=1

#We verify JJ:

counties = ["%.2d" % i for i in range(1,47)]
counties.append('51')
counties.append('52')
inserted_county = CNP[7:9]
if inserted_county in counties:
    pass
else:
    print('JJ invalid')
    v=1

# We verify NNN:
if CNP[9:12].isdigit() and int((CNP)[9:12]) >= 1:
    pass
else:
    print("NNN Not Valid")
    v=1
#We verify the control number
check_number = "279146358279"
sum = 0
control_digit = 0
for i in range(0,12):
    sum += int(check_number[i]) * int(CNP[i])
if sum % 11 == 10:
    control_digit = 1
else:
    control_digit = sum % 11
if control_digit != int(CNP[-1]):
    print("Control digit invalid")
    v=1
try:
    datetime.strptime(CNP[1:7], '%y%m%d')
except ValueError:
    print('Ai introdus o data invalida\nFormatul trebuie sa fie YYMMDD')
    v=1

if v==0:
    print("CNP-ul a fost validat cu succes")
else:
    print("CNP-ul nu a putut fi validat")