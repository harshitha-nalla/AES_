
def Caesar_Cipher(key,msg):
    enc_msg=""
    for i in msg:
        enc_msg+=chr((ord(i)-ord('a')+key)%26 + ord('a'))
    return enc_msg

msg=input("Enter the message: ")
key=4
print(Caesar_Cipher(key,msg))



