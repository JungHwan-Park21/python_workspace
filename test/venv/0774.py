# 1+1
#
# a="hello"
# print(a)
#
#
# a="python"
# print(a*2)
#
# import  def random_pop(data):random
# #
#     number = random.randint(0,len(data)-1)
#     return data.pop(number)
#
# if __name__ == "__main__":
#     data = [1,2,3,4,5]
#     while data:
#         print(random_pop(data))

data=list(range(1,46))

import random
def random_pop(data):
    number = random.randint(0,len(data)-1)
    return data.pop(number)

for i in range(1,7):
    print(random_pop(data))

# import webbrowser
# webbrowser.open("http://google.com")

