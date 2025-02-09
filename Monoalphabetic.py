def mono_alphabetic(msg):
    Letters1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Letters2 = "STABJOWXUVZDFEHGCIKMLNRPQY"
    enc_msg=""
    for c in msg:
        enc_msg+=Letters2[Letters1.index(c)]
    return enc_msg

msg=input("Enter the message:")
msg=msg.upper()
print("The encrypted message is: "+mono_alphabetic(msg))

