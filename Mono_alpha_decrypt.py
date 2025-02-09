def mono_Decrypt(msg):
    Letters1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Letters2 = "ANDREWICKSOHTBFGJLMPQUVXYZ"
    dec_msg=""
    for c in msg:
        dec_msg+=Letters1[Letters2.index(c)]
    return dec_msg

msg=input("Enter the Encrypted message:")
msg=msg.upper()
print("Output: "+mono_Decrypt(msg))
