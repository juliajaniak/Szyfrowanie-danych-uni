from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

tekst=b'sekret'
klucz=b'kryptografiadlat'

aes=AES.new(klucz,AES.MODE_ECB)

szyfr=aes.encrypt(pad(tekst,AES.block_size))
odszyfr=aes.decrypt(pad(szyfr,AES.block_size))

print('\nTekst:',tekst)
print('\nKlucz:',klucz)
print('\nSzyfr:',szyfr)
print('\nOdszyfr:',odszyfr)
