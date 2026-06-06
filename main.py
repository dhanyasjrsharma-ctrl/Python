#indexing
a="harsh"
print(a[2])
print(a[1],a[-4])
print(a[2:5:1])

b="sheriyans"
#for printing only sher
print(b[0:4])
#indexing starts with zero
print(b[5::1])

#type conversion
c=25.67
print(type(c))
d=int(c)
print(type(d))

e="12"
e=int(e)
print(e)

#all are true except 7 values : false,0,0.0,"",[],{},()

print(bool(12))
print(bool("hello"))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(12.56))
