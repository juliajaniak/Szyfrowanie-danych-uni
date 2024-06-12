from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
#cipherblock chaining mode
#potrzebujemy pad

tekst = b'litwoojczyznomojatyjestesjakzdrowieilecietrzebacenictentylkosied'
klucz = b'abcd1234'
iv=     b'12345678'

des=DES.new(klucz,DES.MODE_CBC,iv)
#potrzebujemy iv

szyfr=des.encrypt(pad(tekst,DES.block_size))
#pad to potrzebujemy tekstu i DES.block_size

print('\nTekst:',tekst)
print('\nKlucz:',klucz)
print('\nWektor:',iv)
print('\nSzyfr:',szyfr)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
tekst=b'sekret'
klucz=b'kryptografiadlat'
iv=b'ychcojadoceniaja'
aes=AES.new(klucz,AES.MODE_CBC,iv)
szyfr=aes.encrypt(pad(tekst,AES.block_size))

d_cipher = AES.new(klucz,AES.MODE_CBC,iv)
odszyfr=d_cipher.decrypt(pad(szyfr,AES.block_size))
print('Tekst: ', tekst)
print('Klucz:', klucz)
print('Wektor:' ,iv)
print('Szyfrogram: ', szyfr)
print('Odszyfrowany:', odszyfr)