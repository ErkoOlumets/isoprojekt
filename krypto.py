from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import sys

# 
# try:
#     sisse_failinimi = sys.argv[1]
# except:
#     sisse_failinimi = "tekst_krüpteerimiseks.txt"


################

# inspiratsioon koodile saadud lehelt https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-aes

################
#tekstifaili_nimi  = "tekst_krüpteerimiseks.txt" , key = get_random_bytes(16)

### @reg add HKEY_CURRENT_USER\Software\Classes\*\shell\Krüpteeri\command /f /t REG_SZ /ve /d "\"C:\Program Files (x86)\Thonny\python.exe\" \"C:\Users\Kasutaja\Desktop\Proge\ISO_PROJEKT\ISO_PROJEKT.py\" \"^%1\""


def encrypt(tekstifaili_nimi):
    cd = tekstifaili_nimi[::-1]
    a = cd.index('/')
    uus = cd[a:]
    dr = uus[::-1]
    key = get_random_bytes(16)
    with open(tekstifaili_nimi, encoding="UTF-8") as f:
        data = bytes(f.read(), "UTF-8")

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"{dr}encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()
    
    with open(f"{dr}key.bin","wb") as f:
        f.write(key)

### key = open(r"C:\Users\Kasutaja\Desktop\Proge\ISO_PROJEKT\key.bin", "rb").read(), file_in = open(fr"C:\Users\Kasutaja\Desktop\Proge\ISO_PROJEKT\{bin_fail}", "rb")
def decrypt(v6ti, fail_in):
    cd = v6ti[::-1]
    a = cd.index('/')
    uus = cd[a:]
    dr = uus[::-1]
    key = open(v6ti, "rb").read()
    file_in = open(fail_in, "rb")
    
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    
    
    str_data = data.decode(encoding="UTF-8")
    with open(f"{dr}esialgne.txt", "w", encoding="UTF-8") as f:
        f.write(str_data)
# key = open(r"C:\Users\37253\Desktop\progepraht\projekt\gui\key.bin", "rb").read()
# file_in = open(r"C:\Users\37253\Desktop\progepraht\projekt\gui\krüpteeritud_fail.bin", "rb")
