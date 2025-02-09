
def Key_Matrix(key):
    M = []
    for letter in key:
        if letter not in M:
            M.append(letter)
    Letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in Letters:
        if letter not in M:
            M.append(letter)
    key_matrix = [M[0:5], M[5:10], M[10:15], M[15:20], M[20:25]]
    print(key_matrix)

key="srmapuniversity"
key=key.upper()
Key_Matrix(key)