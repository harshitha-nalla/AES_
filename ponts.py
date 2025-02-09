# import calendar
# print(calendar.weekday(2000,10,15))
# print(calendar.prcal(2004))
# from datetime import datetime as dt
# import pytz
# tz=pytz.timezone('Singapore')
# print(dt.now(tz))
# import numpy as np
# a=np.array([[1,2.5],[2,5]])
# b=np.ones((2,2))
# print(np.multiply(a,b))
#
#CAESAR CIPHER
# import string
# str="hello I am harshitha"
# dic={}
# data=''
# for i in range(len(string.ascii_letters)):
#     dic[string.ascii_letters[i]]=string.ascii_letters[(i+1)%52]
# for i in range(len(str)):
#     if str[i] in dic:
#         data=dic[str[i]]
#     else:
#         data=str[i]
#     print(data,end="")
###BINARY SEARCH USING RECURSION
# def bin(l,x,s,e):
#     if s==e:
#         if l[s]==x:
#             return s
#         else:
#             return -1
#     else:
#         mid=int((s+e)/2)
#         if l[mid]==x:
#             return mid
#         elif l[mid]>x:
#             return bin(l,x,s,mid-1)
#         else:
#             return bin(l,x,mid+1,e)
# l=[4,5,8,67,98,99]
# k=bin(l,99,0,5)
# print(k)
import datetime
dd=datetime.date(2004,10,8)
print(dd)


