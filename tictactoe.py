import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
print(board)
p1= 'x'
p2= 'o'

def place(p):
    while(1):
        row=int(input(" enter row:"))
        col=int(input("enter column:"))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
           break
    board[row - 1][col - 1] = p
    print(board)

def checkr(p):
    for r in range(3):
        cou=0
        for c in range(3):
            if board[r][c]==p:
                cou=cou+1
        if(cou==3):
            print(p,"won")
            return True
    return False
def checkc(p):
    for c in range(3):
        cou=0
        for r in range(3):
            if board[r][c]==p:
                cou=cou+1
        if(cou==3):
            print(p,"won")
            return True
    return False
def checkd(p):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==p:
        print(p,"won")
        return True
    if board[2][2]==board[1][1] and board[1][1]==board[0][0] and board[1][1]==p:
        print(p,"won")
        return True
    return False

def won(p):
    return checkr(p) or checkc(p) or checkd(p)

def play():

    for turn in range(9):
        if turn%2==0:
            print('p1 turn:')
            place(p1)
            if won(p1):
                break
        else:
            print('p2 turn:')
            place(p2)
            if won(p2):
                break

    if not won(p1) and not won(p2):
        print("draw")
play()
# import numpy
# board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
# print(board)
# p1= 'x'
# p2= 'o'
#
# def place(p):
#     while(1):
#         row=int(input(" enter row:"))
#         col=int(input("enter column:"))
#         if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
#             break
#         board[row - 1][col - 1] = p
#         print(board)
# def checkr(p):
#     for r in range(3):
#         cou=0
#         for c in range(3):
#             if board[r][c]==p:
#                 cou=cou+1
#         if(cou==3):
#             print(p,"won")
#             return True
#     return False
# def checkc(p):
#     for c in range(3):
#         cou=0
#         for r in range(3):
#             if board[r][c]==p:
#                 cou=cou+1
#         if(cou==3):
#             print(p,"won")
#             return True
#     return False
# def checkd(p):
#     if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==p:
#         print(p,"won")
#         return True
#     if board[2][2]==board[1][1] and board[1][1]==board[0][0] and board[1][1]==p:
#         print(p,"won")
#         return True
#     return False
#
# def won(p):
#     return checkr(p) or checkc(p) or checkd(p)
#
# def play():
#     for turn in range(9):
#         if turn%2==0:
#             print('p1 turn:')
#             place(p1)
#             if won(p1):
#                 break
#         else:
#             print('p2 turn:')
#             place(p2)
#             if won(p2):
#                 break
#     if not won(p1) and not won(p2):
#         print("draw")
# play()