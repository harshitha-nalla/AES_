import numpy

def find_index(c,key_matrix):
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix[i])):
            if key_matrix[i][j]==c:
                return i, j
    return None
def Encrypt(msg,key):
    M=[]
    encry_msg=""
    for letter in key:
        if letter not in M:
            M.append(letter)
    Letters="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in Letters:
        if letter not in M:
            M.append(letter)
    key_matrix=[M[0:5],M[5:10],M[10:15],M[15:20],M[20:25]]
    print(key_matrix)
    for i in range(0,len(msg),2):
        str=msg[i:i+2]
        r1,c1=find_index(str[0],key_matrix)
        r2,c2=find_index(str[1],key_matrix)
        if r1==r2:
            encry_msg+=key_matrix[r1][(c1+1)%5]
            encry_msg += key_matrix[r2][(c2+1) % 5]
        elif c1==c2:
            encry_msg += key_matrix[(r1 + 1) % 5][c1]
            encry_msg += key_matrix[(r2 + 1) % 5][c2]
        else:
            encry_msg += key_matrix[r1][c2]
            encry_msg += key_matrix[r2][c1]
    return encry_msg

def Decrypt(msg,key):
    M = []
    decry_msg = ""
    for letter in key:
        if letter not in M:
            M.append(letter)
    Letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in Letters:
        if letter not in M:
            M.append(letter)
    key_matrix = [M[0:5], M[5:10], M[10:15], M[15:20], M[20:25]]
    for i in range(0, len(msg), 2):
        str = msg[i:i + 2]
        r1, c1 = find_index(str[0], key_matrix)
        r2, c2 = find_index(str[1], key_matrix)
        if r1 == r2:
            decry_msg += key_matrix[r1][(c1 - 1) % 5]
            decry_msg += key_matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            decry_msg += key_matrix[(r1 - 1) % 5][c1]
            decry_msg += key_matrix[(r2 - 1) % 5][c2]
        else:
            decry_msg += key_matrix[r1][c2]
            decry_msg += key_matrix[r2][c1]
    return decry_msg


msg=input("Enter the message:")
msg = msg.replace(" ","")
if len(msg)%2==1:
        msg+='z'
msg=msg.upper()
msg=msg.replace('J','I')
key = "srmapuniversity"
key=key.upper()
Encrypted_msg=Encrypt(msg,key)
print(Encrypted_msg)
print(Decrypt(Encrypted_msg,key))



