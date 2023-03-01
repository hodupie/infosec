import base64

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

password = "hoduddangkongmom".encode('utf8')
aes = AES.new(password, AES.MODE_ECB)
block_Size = 16

def encrypt(text):
    byted_text = text.encode("utf8")
    padded_text = pad(byted_text, block_Size)
    encrypted_text = base64.b64encode(aes.encrypt(padded_text)).decode('utf-8')
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = aes.decrypt(base64.b64decode(encrypted_text.encode('utf-8')))
    unpadded_text = unpad(decrypted_text, block_Size)
    origin_text = unpadded_text.decode('utf-8')
    return origin_text

print("1. 암호화 \n2. 복호화")
menu = input("메뉴를 선택하세요 ")

if menu == '1':
    text = input("문장 : ")
    encrypted_text = encrypt(text)
    print("암호화 : ", encrypted_text)

elif menu == '2':
    text = input("문장 : ")
    decrypted_text = decrypt(text)
    print("복호화 : ", decrypted_text)
    
else: print("올바르지 않은 메뉴입니다.")
