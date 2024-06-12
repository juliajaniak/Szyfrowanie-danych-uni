#szyfrowanie i deszyfrowanie zdjęcia
#ECB
#porcje po 16bitów

from Crypto.Cipher import AES
klucz=b'aaaabbbbccccdddd'
szyfr=AES.new(klucz,AES.MODE_ECB)
with open("tux.bmp","rb") as f:
    blok = f.read()
    
pad=len(blok)%16-1
blok_przyciety=blok[64:pad]
szyfrogram=szyfr.encrypt(blok_przyciety)
szyfrogram=blok[0:64]+szyfrogram+blok[pad:]
with open("ctux.bmp","wb") as f:
    f.write(szyfrogram)
    
with open("ctux.bmp","rb") as f:
    blok = f.read()
pad=len(blok)%16-1
blok_przyciety=blok[64:pad]
tekst=szyfr.decrypt(blok_przyciety)
tekst=blok[0:64]+tekst+blok[pad:]
with open("dtux.bmp","wb") as f:
    f.write(tekst)