from Crypto.Cipher import DES
#electronic codebook mode

tekst = b'litwoojczyznomojatyjestesjakzdrowieilecietrzebacenictentylkosied'
klucz =b'abcd1234'

des = DES.new(klucz, DES.MODE_ECB)
#tu najpierw inicjujemy ten klucz DES

szyfr = des.encrypt(tekst)
tekst_od = des.decrypt(szyfr)

print('\nTekst: ',tekst)
print('\nKlucz: ',klucz)
print('\nSzyfrogram: ',szyfr)
print('\nTekst odszyf: ',tekst_od)
