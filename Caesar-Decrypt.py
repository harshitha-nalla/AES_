def Caesar_decrypt(msg):
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,26):
        dec_msg=""
        for c in msg:
            if(c==" "):
                dec_msg+=" "
            elif(c.isalpha()):
                if Letters.index(c)-i<0:
                    dec_msg += Letters[(Letters.index(c) - i)+26]
                else:
                    dec_msg += Letters[Letters.index(c) - i]
        print(dec_msg)


msg=input("Enter the Encrypted message: ")
msg=msg.upper()
Caesar_decrypt(msg)