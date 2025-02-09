def Vigenere(key,msg):
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enc_msg=""
    key_count = 0
    for c in msg:
        enc_msg+=Letters[(Letters.index(c)+Letters.index(key[key_count%len(key)]))%26]
        key_count+=1
    return enc_msg

def Decrypt_Vigenere(key,Encrypted_msg):
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dec_msg=""
    key_count=0
    for c in Encrypted_msg:
        if Letters.index(c)-Letters.index(key[key_count%len(key)])<0:
            dec_msg+=Letters[26+(Letters.index(c)-Letters.index(key[key_count%len(key)]))]
        else:
            dec_msg += Letters[(Letters.index(c) - Letters.index(key[key_count % len(key)]))]
        key_count += 1
    return dec_msg

msg=input("Enter the message:")
msg=msg.upper()
key=input("Enter the key: ")
key=key.upper()
Encrypted=Vigenere(key,msg)
print("The encrypted message is: "+Encrypted)
print("The decrypted message is: "+Decrypt_Vigenere(key,Encrypted))


