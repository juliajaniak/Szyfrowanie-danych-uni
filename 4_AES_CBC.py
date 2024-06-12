from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


tekst=b'sekret'
klucz=b'kryptografiadlat'
iv=   b'ychcojadoceniaja'

aes=AES.new(klucz,AES.MODE_CBC,iv)
szyfr=aes.encrypt(pad(tekst,AES.block_size))

print('\nTekst:',tekst)
print('\nKlucz:',klucz)
print('\nWektor:',iv)
print('\nSzyfr:',szyfr)
