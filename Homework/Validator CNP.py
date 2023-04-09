import random

# DATE DE INTRARE
sex='male'
age=1980
month='Jul'
day=9
judet='Timis'
# We find S
if sex=='male':
        if age//100==19:
            s=1
        elif age//100==18:
            s=3
        elif age//100==20:
            s=5

if sex=='female':
    if age // 100 == 19:
        s = 2
    elif age // 100 == 18:
        s = 4
    elif age // 100 == 20:
        s = 6

# We find AA
aa=age%100

# We find LL
months_of_year=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
if month in months_of_year:
    ll=months_of_year.index(month)
# We fin ZZ
if day % 10 == 0:
    zz = day
else:
    zz = f"{day:02d}"
# We find JJ
countries = {
    '01': 'Alba',
    '02': 'Arad',
    '03': 'Arges',
    '04': 'Bacau',
    '05': 'Bihor',
    '06': 'Bistrita-Nasaud',
    '07': 'Botosani',
    '08': 'Brasov',
    '09': 'Braila',
    '10': 'Buzau',
    '11': 'Caras-Severin',
    '12': 'Cluj',
    '13': 'Constanta',
    '14': 'Covasna',
    '15': 'Dambovita',
    '16': 'Dolj',
    '17': 'Galati',
    '18': 'Gorj',
    '19': 'Harghita',
    '20': 'Hunedoara',
    '21': 'Ialomita',
    '22': 'Iasi',
    '23': 'Ilfov',
    '24': 'Maramures',
    '25': 'Mehedinti',
    '26': 'Mures',
    '27': 'Neamt',
    '28': 'Olt',
    '29': 'Prahova',
    '30': 'Satu Mare',
    '31': 'Salaj',
    '32': 'Sibiu',
    '33': 'Suceava',
    '34': 'Teleorman',
    '35': 'Timis',
    '36': 'Tulcea',
    '37': 'Vaslui',
    '38': 'Valcea',
    '39': 'Vrancea',
    '40': 'Bucuresti',
    '41': 'Bucuresti - Sector 1',
    '42': 'Bucuresti - Sector 2',
    '43': 'Bucuresti - Sector 3',
    '44': 'Bucuresti - Sector 4',
    '45': 'Bucuresti - Sector 5',
    '46': 'Bucuresti - Sector 6',
    '47': 'Bucuresti - Sector 7 (desfiintat)',
    '48': 'Bucuresti - Sector 8 (desfiintat)',
    '51': 'Calarasi',
    '52': 'Giurgiu',
}
if judet in countries:
    jj = list(countries.keys())[list(countries.values()).index(judet)]

    # We find NNN
nnn=random.randrange(0,999)

CNP=int(str(s) + str(aa)+str(ll)+str(jj)+str(nnn))
print(CNP)