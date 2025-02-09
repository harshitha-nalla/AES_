from des import DesKey


def Encrypt(msg,key):
    print("The encrypted message is: ")
    print(key.encrypt(msg,padding=True))
    return key.encrypt(msg,padding=True)

def Decrypt(msg,key):
    print("The decrypted message is: ")
    print(key.decrypt(msg,padding=True))

msg=input("Enter the message: ")
key=DesKey(b"srmapuni")
enc_msg=Encrypt(msg,key)
Decrypt(enc_msg,key)






