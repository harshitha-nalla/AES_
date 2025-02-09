# import string
#  li=input('enter name1:')
# li.lower()
#  li.replace(" ","")
# l=list(li)
# mi=input('enter name2:')
# mi.lower()
# mi.replace(" ","")
# m=list(mi)
# def matching(l,m):
#     for i in range(len(l)):
#         for j in range(len(m)):
#             if l[i]==m[j]:
#                 c=l[i]
#                 l.remove(c)
#                 m.remove(c)
#                 new=l+['*']+m
#                 return [new,True]
#     new=l+['*']+m
#     return [new,False]
# pro=True
# while pro:
#     ret=matching(l,m)
#     pro=ret[1]
#     li=ret[0]
#     k=li.index('*')
#     l=li[:k]
#     m=li[k+1:]
# c=len(l)+len(m)
# fla=['friends','love','affection','marriage','enemies','sisters']
# s=(c%len(fla))-1
# while len(fla)>1:
#
#     if s>=0:
#         right=fla[s+1:]
#         left=fla[:s]
#         fla=right+left
#     else:
#         fla=fla[:len(fla)-1]
# print(fla[0])
#
# def matching(l, m):
#     for i in range(len(l)):
#         for j in range(len(m)):
#             if l[i] == m[j]:
#                 c = l[i]
#                 l.remove(c)
#                 m.remove(c)
#                 return l, m, True
#     return l, m, False
#
# li = input('enter name1:').lower().replace(" ", "")
# l = list(li)
#
# mi = input('enter name2:').lower().replace(" ", "")
# m = list(mi)
#
# pro = True
# while pro:
#     l, m, pro = matching(l, m)
#     k = l.index('*')
#     l = l[:k]
#     m = l[k + 1:]
#
# c = len(l) + len(m)
# fla = ['friends', 'love', 'affection', 'marriage', 'enemies', 'sisters']
# s = (c % len(fla)) - 1
#
# while len(fla) > 1:
#     if s >= 0:
#         right = fla[s + 1:]
#         left = fla[:s]
#         fla = right + left
#     else:
#         fla = fla[:len(fla) - 1]
#
# print(fla[0])
# import random
# l=[1,3,2,4,8]
# random.shuffle(l)
# print(l)
# l=[1,4,5,7,8]
# m=[]
# for i in range(max(l)):
#     m.append(0)
# for k in l:
#     m.insert(k,k)
#
# print(m[:max(l)+1])
# # import calendar
# print(calendar.isleap(2004))
#
a=int(input())
b=int(input())
c=int(input())
l=[]
l.append(a)
l.append(b)
l.append(c)
k=max(l)
l.remove(k)
if k**2==l[0]**2+l[1]**2:
    print("right ")
else:
    print("no")

