from des import DesKey
key= DesKey(b"Hello I am fromS")
print(key.encrypt(b"Hello",padding=True))

def encr