#predefined-functions-in-list
#1.append:used to add element at the end  of the list syntax listobj.append(value)
a=[10,45,"kiran",67,"hyd","34",87]
print(a,type(a),id(a))
a.append("durga")
a.append(45)
a.append(97)
print(a)
a.append(True)
print(a)
#2.insert:used to add value based on index  listobj(index,value)
a.insert(0,"hello")
print(a)
a.insert(len(a)-1,"bye")
print(a)
#3.remove :remove value
a.remove("bye")
print(a)
a.remove("durga")
print(a)
#a.remove('har')---this gives value error because value is not there
#list().remove(89)---this gives value error because value is not there
#[].remove(8)---this gives value error because value is not there
#4.pop(index)
a.pop(0)
print(a)
a.pop(-1)
print(a)
#a.pop(15)---this gives an error because index is not there-indexerror
#[].pop(0)---this gives an error because index is not there-indexerror

#5.pop()-this  removes last element and returned
print(a.pop())
print(a.pop())
#print([].pop())-->IndexError: pop from empty list
#6.clear()
a.clear()
print(a)
print([].clear())#when you call clear() on emptylist you get "None"
#7.del operator
a=[10,45,"kiran",67,"hyd","34",87]
del a[0]
print(a)
del a[1:3]
print(a)
#del a
#print(a)--->we get name error because a is deleted
#del "kiran"[0]--TypeError: 'str' object doesn't support item deletion
#del "kiran"[0:2]--TypeError: 'str' object does not support item deletion
b="kiran"
del b
#print(b)-->NameError: name 'b' is not defined
#8.copy() a)shallow copy
a=[10,45,"kiran",67,"hyd","34",87]
b=a.copy()
print(a,id(a))
print(b,id(b))
a.append("ki")
b.append("hello")
print(a)
print(b)
#deep copy()
c=[1,2,3,4,43,43,33]
d=c
print(id(c),id(d))
c.append("bye")
print(c)
print(d)
#9.index()
e=[10,20,30,40,10,40,20,60]
print(e.index(10))
#print(e.index(70))-->ValueError: list.index(x): x not in list
for x in enumerate(e):
    print(x)

for i,v in enumerate(e):
    print(i,"-->",v)
print("------------------------------------")
for i,v in enumerate(e):
    if(v==10):
        print(i,'-->',v)


#TypeError: 'int' object is not iterable
"""f=100
for i,v in enumerate(f):
    print(i,v)"""
#10.count()
e=[10,20,30,40,10,40,20,60]
print(e.count(40))
print(e.count(100))
g="1234043002011"
print(list(g).count("0"))
print(list(g).count("1"))

#11.reverse
e=[10,20,30,40,10,40,20,60]
e.reverse()
print(e)

#12.sort
e=[10,20,30,40,10,40,20,60]
e.sort()
print(e)
e.sort(reverse=True)
print(e)
e.sort(reverse=False)
print(e)
g=["kfdkfj","dijsh","kjs","snh","djiid"]
g.sort()
print(g)
g.sort(reverse=True)
print(g)
g.sort(reverse=False)
print(g)

#13.extend
l=[10,40,577,67,99,454,99,98]
m=[6,3,9,5,0,3,3,3]
l.extend(m)
print(l)

l=[10,40,577,67,99,454,99,98]
m=[6,3,9,5,0,3,3,3]
k=[9,4,2,4,2,4,22]
l.extend(m)
l.extend(k)
print(l)

#2nd approach using+
l=[10,40,577,67,99,454,99,98]
m=[6,3,9,5,0,3,3,3]
k=[9,4,2,4,2,4,22]
l=l+m+k
print(l)




