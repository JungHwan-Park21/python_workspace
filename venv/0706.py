# # a="Hello World"
# # print(a)
#
# a=3
# b=4
# print(a*b)
#
# print("%10s"% "hi")
# print("%10s"% "adv")
# print("%10s"% "www")
# print("%-10spark"% "hi")
# print("%-10spark"% "ㅇㅇㅇ")
# print("%-10spark"% "sldoe")

# print("i ate {0} apples.so i was sick for {1} days.".format(number, day))

print("="*24)
print("{0:^20}".format("학사관리"))
print("="*24)


print(",".join('abcd'))
print(",".join(['홍길동','컴튜터공어','서울','남']))

a="       hi        "
print(a)
print(a.lstrip())
print(a.strip())
print(a.rstrip())

a="Life is too short"
b="a:b:c:d"
print(a)
print(a.split())
print(b)
print(b.split(';'))

a=[1,2,['a','b',['life','is']]]
print(a)
print(a[2])
print(a[2][2][0])

a=[1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a=[1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
print(a)

# t1=(1,2,3)
# del t1[0]

a={1:'a'}
a[2] ='b'
print(a)

a['name']='pey'
print(a)

a[3]=[1,2,3]
print(a)

del a[1]
print(a)

a={1:'a',2:'b'}
print('a:2')

a={'name':'pey','phone':'01022232321','birth':'1118'}
for k in a.keys():
    print(k)
    print(a[k])

a={"name":"pey","phone":"01022322232","birth":"1118"}
for k in a.keys():
    print(k)
    print(a[k])

s2=set("hello")
print(s2)
s1=set([1,2,3,1,1,1,])
print(s1)

s1=set([1,2,3])
s1.update([4,5,6])
print(s1)

s1=set([1,2,3])
s1.remove(2)
print(s1)

a=[1,2,3,4]
while a:
    print(a.pop())

bool('python')

a=[1,2,3]
print(id(a))
b=a
print(id(a))
print(id(b))
a[1]=4
print(a)
print(b)

a=[1,2,3]
b=a[:]
print(id(a))
print(id(b))

from copy import copy
a=[1,2,3]
b=copy(a)
print(b)

a,b=('python','life')
print(a)
print(b)

a=b='pythpn'
a=3
b+5
