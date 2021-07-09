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

# a=b='pythpn'
# a=3
# b+5

# pocket=['paper','cellphone','money']
# if 'money' in pocket:
#     print("택시를 타고가라")
# else:
#     if card:
#         print("택시를 타고가라")
#     else:
#         print("걸어가라")

# treeHit=0
# while treeHit<10:
#     treeHit=treeHit+1
#     print("나무를 %d번 찍었습니다." %treeHit)
#     if treeHit==10:
#         print("나무 넘어갑니다")
#
# coffee=10
# while True:
#     money=int(input("돈을 넣어주세요: "))
#     if money ==300:
#         print("커피를 줍니다.")
#         coffee=coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
#         coffee=coffee-1
#     else:
#         print("돈을 다시 돌려주고 커리를 주지 않습니다.")
#         print("남은 커피의 양은%d개 입니다"%coffee)
#     if coffee==0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break
#
# marks=[90,25,67,45,80]
#
# number=0
# for mark in marks:
#     number=number+1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다."%number)
#     else:
#         print("%d번 학생은 불합격입니다"%number)
#
#
# add=0
# for i in range(1,11):
#     add=add+i
#
# print(add)
#
# marks = [90,25,68,54,80]
# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다 합격입니다~"% (number+1))
#
#
# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end=" ")
#     print('')
#
# for i in range(2,10):
#     for j in range(1,10):
#         print("%d*%d=%2d" %(i,j,i*j),end=" ")
#     print('')
#
# a=[1,2,3,4]
# print([num*2 for num in a])

# result=[x*y for x in range(2,10)
#         for y in range(1,10) ]
# print(result)
#
# def add_mul(choice, *args):
#     if choice=="add":
#         result=0
#         for i in args:
#             result=result+i
#     elif choice=="mul":
#         result=1
#         for i in args:
#             result=result+i
#     return  result

class Calculator:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result += num
        return  self.result
cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first + self.second
        return  result
    def mul(self):
        result=self.first * self.second
        return result
    def sub(self):
        result=self.first - self.second
        return result
    def div(self):
        result=self.first / self.second
        return result

a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(3.8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
