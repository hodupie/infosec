import hashlib

def MD5_hash(path):
    f = open(path, 'rb')
    data = f.read()
    hash = hashlib.md5(data).hexdigest()
    return hash


file_name = input("파일 이름을 넣으세요. ")
hash_value = MD5_hash(file_name)
print("파일의 해시 값(md5)은 ", hash_value)