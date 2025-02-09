n=int(input("enter the number:"))
def magicsquare(n):
    for i in range(n):
        m=[]
        for j in range(n):
            l=[]
            l.append(0)
        m.append(l)
   for i in range(n):
       for j in range(n):
           print(m[i][j])

magicsquare(3)