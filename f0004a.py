név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
évszám = input('Hányadik évben élünk? ')
évszám = int(évszám)
születési_év = évszám - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')