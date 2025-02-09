n = int(input("enter the number:"))


def magicsquare(n):
    m = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        m.append(l)
    c = 1
    i = n // 2
    j = n - 1
    k = n * n
    while (c <= k):
        if (i == -1 and j == n):
            i = 0
            j = n - 2
        elif (i < 0):
            i = n - 1
        elif (j == n):
            j = 0
        elif (m[i][j] != 0):
            j = j - 2
            i = i + 1
            continue
        else:
            m[i][j] = c
            c = c + 1
            i = i - 1
            j = j + 1

    for i in range(n):
        for j in range(n):
            print(m[i][j], end=" ")
        print()


magicsquare(n)
#magic constant=(n*(n*n+1))/2