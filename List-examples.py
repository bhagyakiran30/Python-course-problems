#list example --4syntaxes
#---->syntax-listobj=[a1,a2,a3--an]--
a=[10,"kiran","hyd",89,"hj"]
print(a,type(a))

#indexing
print(a[2],a[3])
print(a[-2],a[-4],type(a[-2]))
print(type(a[1]))

#print(a[7])   #this gives an error

#slicing
print(a[0:3],type(a[1:7]))
print(a[::2])
print(a[2:4])

# address of a
print(id(a))

#item-assignment through index based
a[0]="kiran"
a[1]=10
print(a,id(a))

#item-assignment through slice based
a[0:3]=["hyd","kiran",10]
print(a,id(a))

#--2-syntax listobj=list(iterable-obj)
b="bhagyakiran"
print(list(b))

#--3-syntax listobj=list([iterable-obj])
b="bhagyakiran"
print(list([b]))

#--4-syntax listobj=list([Non-iterable-obj])
c=10
# print(list(c))  #TypeError: 'int' object is not iterable
print(list([c]))

#empty-list
d=[]
print(len(d))
e=list()
print(len(e))