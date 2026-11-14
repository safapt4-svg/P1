# import p1 as q
# import datetime
# import math
# c=q.a + q.b
# print (c)
# x=datetime.datetime.now()
# print(x.strftime("%a"))
# x=datetime.datetime.now()
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%b"))
# print(x.strftime("%d"))
# print(x.strftime("%D"))
# print(x.strftime("%Y"))
# print(x.strftime("%y"))
# print(x.strftime("%x"))
# print(x.strftime("%c"))
# x=min(2,4,5)
# print(x)
# x=(2,3,4,5,6,8)
# print (max(x))
# print (len(x))
# a=-2533
# print(abs(a))
# c=pow(2,3)
# print(c)
# d=pow(54,87)
# print(d)
# x=math.sqrt(225)
# print(x)
# a=math.ceil(3.5)
# b=math.floor(3.5)
# print(a)
# print(b)
# FILE HANDLING
# a=open(r'C:\Users\dell\Desktop\testfile.txt')
# print(a.read())
# x=open(r'C:\Users\dell\Desktop\t2.txt')
# print(x.read())
# with open(r'C:\Users\dell\Desktop\t2.txt')as i:
#     x=i.read()
#     print(x)
# a=open(r'C:\Users\dell\Desktop\t2.txt')
# print(a.read())
# with open(r'C:\Users\dell\Desktop\t2.txt')as j:
#     m=j.read()
#     print(m)
# write in a file
# 
# with open(r'C:\Users\dell\Desktop\t2.txt','w')as k:
#     k.write('hi my name is hsgsg\n hi  \n hello')
    
# with open(r'C:\Users\dell\Desktop\t2.txt')as k:
#     print(k.readline(2))
# x=math.pi
# print(x)
# def isprime(a):
#     if a<=1:
#         return False
#     if a==2:
#         return True
#     if a %2==0:
#         return False
#     for i in range(3,math.isqrt(a)+1,2):
#         if a%i==0:
#             return False
#         return True
# print(isprime(11))

#file(
# a=open(r'C:\Users\dell\Desktop/mytext.txt')
# print(a.read())
# with open(r'C:\Users\dell\Desktop/mytext.txt','w')as p:
#     p.write('hi')
# with open(r'C:\Users\dell\Desktop/mytext.txt')as p:
#     print(p.readline(3))
# with open(r'C:\Users\dell\Desktop/mytext.txt','a')as p:  
#         p.write("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        
# with open(r'C:\Users\dell\Desktop\mytext.txt') as p:
#     content = p.read()
#     print(content)
#     linecount = len(content.splitlines())
#     print(linecount)

# x = open(r'C:\Users\dell\Downloads\createfile.txt','x')
# x = open(r'C:\Users\dell\Downloads\createfiless.py','x')
# # x = open(r'C:\Users\dell\Downloads\createfile1.html','x')
# x=open(r'C:\Users\dell\Downloads\sfile.txt','x')

# with open(r'C:\Users\dell\Downloads\sfile.txt','a')as j:
#     j.write('gshw jqjwgb asdd')
# with open(r'C:\Users\dell\Downloads\sfile.txt')as j:
#     print(j.read())
# import os
# os.remove(r'C:\Users\dell\Downloads\sfile.txt')

# FILES
# X=open(r'C:\Users\dell\Downloads\student.txt','x')
# with open(r'C:\Users\dell\Downloads\student.txt','w') as f:
#     f.write('students')
# with open(r'C:\Users\dell\Downloads\student.txt') as f:
#     print(f.read())
# names=['john','anna','aju','alice']
# with open(r'C:\Users\dell\Downloads\student.txt','a') as f:
#     for name in names:
#         f.write(name + '\n')
#         print(f.read)
# print(f"Total characters: {len(data)}")
# with open(r'C:\Users\dell\Downloads\student.txt') as file:
#     # for x in f:
#     #     print(x)
#    print(f.readline())
#    print(f.readline())
# word_count = 0

# with op(r'C:\Users\dell\Downloads\student.txt') as file:
#     for line in f:
#         # Split the current line and add its length to the total
#         word_count += len(line.split())
# print(f"Tot
#  longest=max(file,key=len)
# print(f"Longest line: {longest}")
# print(f"Length: {len(longest)}")
# searching="jhon"
# with open(r'C:\Users\dell\Downloads\student.txt') as file:
#     content=file.read()
#     count=content.count(searching)
#     print(f"The word '{searching}' appears {count} times in the file.")


import numpy as np
    
# x = np.array(45)
# x1 = np.array([1, 2, 3, 4, 5])
# print(x1[-4:-1])
# # print(x1[0,1])
# print(x1[0])
# print(x1[2]+x1[3])
# x2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(x2[1,1])
# x3 = np.array([[[1, 2], [3, 4]]])
# print(x)
# print(type(x))
# print(x.ndim)
# print(x1)
# print(type(x1))
# print(x1.ndim)
# print(x2)
# print(type(x2))
# print(x2.ndim)
# print(x3)
# print(type(x3))     
# print(x3.ndim)


# a=np.array(23)
# print(a)
# print(type(a))
# print("dimension is",a.ndim)

# b=np.array([1,23,34,45])
# print(b)
# print(type(b))
# print("dimension is",b.ndim)

# c=np.array([[1,2,3],[3,4,67],[45,67,88]])
# print(c)
# print(type(c))
# print('dimension is',c.ndim)

# d=np.array([[[1,2,3],[34,56,67],[34,56,77]]])
# print(d)
# print(type(d))
# print('dimension is',d.ndim)

# a=np.array([[1,23,4],[4,5,6]])
# print(a[0,2])

# b=np.array([[[1,23,4],[4,5,6]],[[3,5,6],[45,67,32]]])
# print(b[1,0,0])
# c=np.array([[[1,23,34],[34,56,67],[34,56,78]]])
# print(c[0,2,2])
# d=np.array([[[1,23,34],[34,56,67]],[[234,667,7],[34,56,78]],[[234,45,66],[456,23,56]]])
# print(d[2,1,2])

# SLICING
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[:3])
# print(a[3:])
# print(a[1:4])
# print(a[4:7])
# print(a[-7:-1])
# print(a[-10:-1])
# print(a[-10:-8])
# print(a[:-3])
# print(a[-3:])

#numpy questions

# 1 
# a=np.array([10,20,30,40,50])
# print(a)

# #2
# b=np.arange(1,21)
# print(b)

# c=np.zeros(10)
# print(c)

# d=np.zeros(10,dtype=int)
# print(d)

# e=np.ones(10,dtype=int)
# print(e)

# f=np.arange(2,21,2)
# print(f)

# g=np.arange(2,21)
# q=g[g%2==0]
# print(q)

# m=np.full((3,3),5)
# print(m)

# n=np.array([[1,23,4],[23,45,12],[34,56,2],[3,40,6]])
# print(n.ndim)
# print(n.size)
# print(n[0,0])
# print(n[3,2])
# print(n[0,2])
# print(n[3,1])

# z=np.array([21,23,34,40,80,23])
# z[z==40]=100
# print(z)
# z[z==80]=800
# print(z)
# print(z[2:5])
# n=np.array([[1,23,4],[23,45,12],[34,56,2],[3,40,6]])
# print(n[0])
# z=np.array([3,46,7,1,5,72,7,8,9])
# print(z[:4])
# print(z[3:])
# print(z[1:9:2])

# a=np.array(['sd','sdf','sdfg','sdfgh','sdfghj'])
# print(a.dtype)

# z=np.array([3,46,7,1,5,72,7,8,9])
# print(z.dtype)

# ar=np.array([True,False,True,True,False])
# print(ar.dtype)

# a=np.array([2,3,4,65,5])
# b=np.array([3,46,7,8,8])
# c=a+b
# print(c)

# a=np.array([2,4,3,1])
# b=np.array([10,3,5,6])
# c=a-b
# print(c)

# a=np.array([2,4,3,1])
# b=np.array([10,3,5,6])
# c=a*b
# print(c)

# a=np.array([14,24,20])
# b=np.array([7,12,5])
# c=a/b
# print(c)

# x=np.array([14,24,20],dtype=float)
# print(x)

# y=np.array([2,4,6])
# square=np.square(y)
# print(square)
# z=np.array([2,4,6])
# square=z**2
# print(square)
# z=np.array([2,4,6])
# square=z**3
# print(square)

# temperature=np.array([43,45,67,31,30,29,28])
# high=temperature[temperature>30]
# print('temperature>30 are:',high)

# float=np.array([1.23,23.45,87.67],dtype=int)
# print('int array is:',float)
# a=np.array([21,1,23,45,67])
# new=a[a>20]
# print(new)

# b=np.array([2,3,4])
# b=b*5
# print(b)

# c=np.array([23,34,67,1,2,3])
# c[c>20]=100
# print(c)

#copy and view
# a=np.array([2,3,6,8])
# b=a.copy()
# a[3]=100
# print(a)
# print('b is:',b)


# a=np.array([2,3,6,8])
# b=a.view()
# a[3]=100
# print(a)
# print('b is:',b)

#iterating in numpy
# a=np.array([[1,2,3,3],[4,5,6,7]])
# for x in a:
#     print(x)#converted 2d to 1d array

    
# a=np.array([[1,2,3,3],[4,5,6,7]])
# for x in a:
#      for y in x:
#          print(y)

# a=np.array([[[1,2,3,4],[4,5,6,7]]])
# for x in a:
#      for y in x:
#             for z in y:
#                 print(z)

#joining numpy arrays
# a=np.array([1,23,4,5])
# b=np.array([3,5,7,8])
# c=np.concatenate((a,b))
# print(c)

# a=np.array([[1,23,4,5],[3,5,6,4]])
# b=np.array([[3,5,7,8],[3,4,5,6]])
# c=np.concatenate((a,b))
# print(c)


# a=np.array([[1,23,4,5],[3,5,6,4]])
# b=np.array([[3,5,7,8],[3,4,5,6]])
# c=np.concatenate((a,b),axis=1)
# print(c)

# a=np.array([[[1,23,5],[3,5,6]],[[1,2,3],[2,3,4]]])
# b=np.array([[[3,7,8],[3,5,6]],[[2,5,6],[3,5,6]]])
# c=np.concatenate((a,b),axis=1)
# print(c)

# hstack,vstack,dstack
# a=np.array([1,23,4,5])
# b=np.array([3,5,6,7])
# c=np.hstack((a,b))
# print(c)
# a=np.array([1,23,4,5])
# b=np.array([3,5,6,7])
# c=np.vstack((a,b))
# print(c)
# a=np.array([1,23,4,5])
# b=np.array([3,5,6,7])
# c=np.dstack((a,b))
# print(c)

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# c=np.hstack((a,b))
# print(c)

# x=np.array([10,20])
# y=np.array([30,40])
# z=np.array([50,60])
# w=np.hstack((x,y,z))
# print(w)

# a=np.array([[2,4],[6,8]])
# b=np.array([[1,3],[5,7]])
# c=np.hstack((a,b))
# print(c)


# a=np.array([[2,4],[6,8]])
# b=np.array([[1,3],[5,7]])
# c=np.concatenate((a,b),axis=1)
# print(c)
# print('shape of resulting array is:', np.shape(c))


# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.vstack((a,b))
# print(c)

# a=np.array([10,20])
# b=np.array([30,40])
# c=np.array([50,60])
# d=np.vstack((a,b,c))
# print(d)

# a=np.array([[2,4,7],[6,8,2]])
# b=np.array([[1,3,3],[5,7,6]])
# c=np.vstack((a,b))
# print(c)
# print('shape is:',np.shape(c))

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# c=np.dstack((a,b))
# print(c)

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# c=np.array([[1,2],[3,5]])
# c=np.dstack((a,b,c))
# print(c)
# print('shape is:',np.shape(c))

# a=np.array([[11,22],[33,44]])
# b=np.array([[55,66],[77,88]])
# c=np.dstack((a,b))
# print(c)
# print('shape is:',np.shape(c))
# print('dimension is:',c.ndim)

# a=np.array([[11,22],[33,44]])
# c=np.sum(a)
# print(c)

# split/search/sort
# a=np.array([[[1,23,5],[3,5,6]],[[1,2,3],[2,3,4]]])
# new=np.array_split(a,3)
# print(new)

# a=np.array([23,34,56,7,345,78,4,2,4,5])
# new=np.array_split(a,6)
# print(new)

# a=np.array([[[1,23,5],[3,5,6]],[[1,2,3],[2,3,4]]])
# new=np.array_split(a,3,axis=1)
# # # print(new)
# print(new[0])
# # print(new[1])
# print(new[2])

# a=np.array([1,23,4,5,67,8,8,8,9,2,3,4,56,6,7,6])
# b=np.where(a==8)
# print(b)

# a=np.array([1,45,6,8,9])
# b=np.where(a%2==0)
# print(b)

# a=np.array([1,45,6,8,9])
# b=np.where(a%2!=0)
# print(b)

# a=np.array([1,6,6,8,45])
# b=np.searchsorted(a,45)
# print(b)

# a=np.array([1,46,6,8,45])
# b=np.searchsorted(a,46)
# print(b)

# a=np.array([1,46,6,8,45])
# b=np.searchsorted(a,46,side='right')
# print(b)
# a=np.array([1,46,6,8,45])
# b=np.searchsorted(a,45,side='right')
# print(b)

# a=np.array([[[1,23,5],[3,5,6]],[[1,2,3],[2,3,4]]])
# b=a.reshape(-1)
# print(b)

# a=np.array([[1,23,5],[3,5,6],[2,3,4]])
# b=a.reshape(-1)
# print(b)

# a=np.array([1,14,45,34])
# b=np.where(a>15)
# print(b)

# search/sort/filter
# a=np.array([45,12,89,34,7,56])
# b=np.sort(a)
# rev=b[::-1]#descending order
# print(b)
# print(rev)

# a=[[5,2,8],[9,1,4],[7,6,3]]
# b=np.sort(a,axis=0)#sorts column
# c=np.sort(a,axis=1)#sorts rows
# print(c)
# print(a)
# print(b)


# a=np.array([1,14,45,34,2,43,5,23,72,11,89])
# b=np.sort(a)
# print(b)

# a=np.array([1,2,4,5,6,40])#this will return all index value where even number appears in the array
# b=np.where(a%2==0)
# print(b)
# c=np.where(a==40)
# print('the value 40 is in index:',c)
# print(c)

# a=np.arange(0,101)
# b=np.where(a%7==0)
# print(b)

# q=np.array([1,2,10,45,10,10])
# c=np.where(q==10)
# print('the value 10 is in index:',c)

# q=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# c=q[q>6]
# print(c)

# arr = np.arange(1, 101)
# filtered_elements = arr[(arr > 40) & (arr < 80)]
# print(arr)

# ar=np.array([12,-1,-34,34,56,7])
# p=ar[ar>0]
# n=ar[ar<0]
# print('positives:',p)
# print('negatives:',n)

# arr = np.array([41, 42, 43, 44])
# filter_arr = []
# for element in arr:
#   if element > 40:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

#PANDAS
import pandas as pd
# x=pd.read_csv(r"C:\Users\dell\Downloads\democsv\democsv.csv")
# # print(x)
# # a=x['Subject']
# # print(a)
# # b=x['STATUS']
# # print(b)
# y=pd.DataFrame(x)
# print(y)

# x=pd.read_excel(r"C:\Users\dell\Downloads\1mb.xlsx")
# print(x)

# y=pd.read_json(r"C:\Users\dell\Downloads\sample1.json")
# print(y)
#pandas data analysing

# a=pd.read_csv(r"C:\Users\dell\Downloads\democsv\democsv.csv")
# print(a.head())
# print(a.head(10))
# print(a.tail())
# print(a.tail(23))

import matplotlib.pyplot as plt
# a=np.array([1,2,3,4,5,6])
# b=np.array([10,20,30,40,50,60])
# # plt.plot(a,b)
# plt.title("student marks")
# plt.xlabel("subject")
# plt.ylabel("marks")
# plt.grid(True)
# plt.bar(a,b)
# plt.scatter(a,b)
# plt.hist(a,b)
# plt.barh(a,b)
# plt.stem(a,b)
# plt.fill_between(a,b)
# plt.stackplot(a,b)
# plt.plot(a,b,label="marks")
# plt.legend()
# plt.show()

# SUBPLOT
# a=np.array([1,2,3,4,5])
# b=np.array([3,4,5,6,7])
# plt.subplot(2,3,1)
# plt.plot(a,b)
# a=np.array([1,2,3,4,5])
# b=np.array([11,23,2,34,5])
# plt.subplot(2,3,2)
# plt.plot(a,b)
# a=np.array([1,2,3,4,5])
# b=np.array([3,4,5,6,7])
# plt.subplot(2,3,3)
# plt.plot(a,b)
# a=np.array([1,2,3,4,5])
# b=np.array([3,4,5,6,7])
# plt.subplot(2,3,4)
# plt.plot(a,b)
# a=np.array([1,2,3,4,5])
# b=np.array([3,4,5,6,7])
# plt.subplot(2,3,5)
# plt.plot(a,b)
# plt.show()

# x=pd.read_csv(r"C:\Users\dell\Downloads\student_marks.csv")
# m=pd.DataFrame(x)
# print(m)
# s=m['Student']
# y=m['Science']
# print(y)
# plt.title("student marks")
# z=m['Math']
# plt.xlabel("student")
# plt.ylabel("Marks")
# plt.plot(s,z) 
# plt.bar(s,z)
#plt.scatter(y,z)
# plt.show()

#student mark analysis
# x=pd.read_csv(r"C:\Users\dell\Downloads\student_marks.csv")
# print(x)
# x['Total'] = x['Math'] + x['Science'] + x['English']+x['Computer']
# result=np.where(x['Total']>=270,'Pass','Fail')
# average=x[['Math','Science','English','Computer']].mean(axis=1)
# top_performers=x.nlargest(3,'Total')
# # pass_fail_count=x['Total'].apply(lambda x: 'Pass' if x>=270 else 'Fail').value_counts()
# print("subject wise average:",average)
# print("top performers:",top_performers)
# print("pass/fail count:",pass_fail_count)

# data cleaning
# a=pd.read_csv(r"C:\Users\dell\Downloads\ipl_uncleaned_practice_dataset.csv")
# b=pd.DataFrame(a)
# print(b)
# a["Runs"] = a["Runs"].fillna(a["Runs"].mean())
# a["Season"] = a["Season"].replace({"Two Thousand Twenty Five": "2025"})
# a["Season"] = pd.to_numeric(a["Season"], errors="coerce")
# a["Runs"] = pd.to_numeric(a["Runs"], errors="coerce")
# a["Team"] = a["Team"].str.strip().str.upper()
# a["Winner"] = a["Winner"].str.strip().str.upper()
# print(a)
# a = a.drop_duplicates()
# a["Team"] = a["Team"].str.strip().str.upper()
# a["Winner"] = a["Winner"].str.strip().str.upper()
# a["Season"] = a["Season"].replace(
#     {"Two Thousand Twenty Five": "2025"}
# )
# a["Season"] = pd.to_numeric(a["Season"])
# a["Runs"] = pd.to_numeric(a["Runs"], errors="coerce")
# a["Runs"] = a["Runs"].fillna(a["Runs"].mean(), errors="coerce")
# a["Season"] = a["Season"].fillna(a["Season"].mode()[0])
# a["Team"] = a["Team"].fillna("UNKNOWN")
# a["Winner"] = a["Winner"].fillna("UNKNOWN")
# print(a)

#SALES DATA CLEANING
df=pd.read_csv(r"C:\Users\dell\Downloads\uncleaned_sales_data.csv")
print(df)
m=df.fillna({
    "Date": "2026-07-13",
    "Region": "Unknown",
    "Salesperson": "Not Assigned"
})
print(m)
m["Region"] = m["Region"].str.strip().str.upper()
m["Quantity"] = pd.to_numeric(m["Quantity"], errors="coerce")
m["UnitPrice"] = pd.to_numeric(m["UnitPrice"], errors="coerce")
#df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
m["Salesperson"] = m["Salesperson"].str.strip().str.title()
print(m)
x=m.to_csv(r"C:\Users\dell\Desktop\datacleaning\cleanedsalesdata.csv", index=False)
# # print("\nCleaned Dataset")
print(x)


