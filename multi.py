import threading
import os
import time

ciag=input("podaj ciag znakow: ")
try:
    num = int(input("podaj liczbe procesow od 1 do 8: "))
except(ValueError):
    num = 2



p1=len(open("320.txt","r",errors='ignore').readlines())

p2=len(open("321.txt","r",errors='ignore').readlines())
p3=len(open("322.txt","r",errors='ignore').readlines())
p4=len(open("323.txt","r",errors='ignore').readlines())
p5=len(open("324.txt","r",errors='ignore').readlines())
p6=len(open("325.txt","r",errors='ignore').readlines())
p7=len(open("326.txt","r",errors='ignore').readlines())
p8=len(open("327.txt","r",errors='ignore').readlines())
p9=len(open("328.txt","r",errors='ignore').readlines())
p10=len(open("329.txt","r",errors='ignore').readlines())
p11=len(open("330.txt","r",errors='ignore').readlines())
p12=len(open("331.txt","r",errors='ignore').readlines())
p13=len(open("332.txt","r",errors='ignore').readlines())
p14=len(open("333.txt","r",errors='ignore').readlines())
p15=len(open("334.txt","r",errors='ignore').readlines())
p16=len(open("335.txt","r",errors='ignore').readlines())
p17=len(open("336.txt","r",errors='ignore').readlines())
p18=len(open("337.txt","r",errors='ignore').readlines())
p19=len(open("338.txt","r",errors='ignore').readlines())
p20=len(open("339.txt","r",errors='ignore').readlines())
#print(type(open("339.txt","r",errors='ignore').readlines()))
book_names = ['3' + str(x + 20) + '.txt' for x in range(20)]
books = [open(x, 'r', errors='ignore').readlines() for x in book_names]
#print("Books len" + )
count=p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20
#print (count)

podzial=int(count/num)
#print (podzial)

tasks = [str() for x in range(num)]
#print(tasks)
temp = num - 1
for book in books:
    for line in book:
        try:
            if len(tasks[temp]) <= podzial:
                try:
                    tasks[temp] += line
                except(IndexError):
                    pass
            else:
                temp -= 1
                try:
                    tasks[temp] += line
                except(IndexError):
                    pass
        except(IndexError):
            pass
def count_occurances(file, pattern):
    ans = file.count(pattern)
    return ans
results = []
for process in range(num):
    pid = os.fork()
    if pid == 0:
        res = count_occurances(tasks[process], ciag)
        if res not in results:
            results.append(res)
        os._exit(0)
    else:
        res = count_occurances(tasks[process], ciag)
        if res not in results:
            results.append(res)

print(results)