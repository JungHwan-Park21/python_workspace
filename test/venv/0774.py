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
# # if __name__ == "__main__":
# #     data = [1,2,3,4,5]
# #     while data:
# #         print(random_pop(data))
#
# data=list(range(1,46))
#
# import random
# def random_pop(data):
#     number = random.randint(0,len(data)-1)
#     return data.pop(number)
#
# for i in range(1,7):
#     print(random_pop(data))
#
# # import webbrowser
# # webbrowser.open("http://google.com")
#
# # a, b = input().split(':')
# # print(a, b, sep=':')
#
# a="당첨을 기원합니다"
# print(a)

# ## 날짜반복
# from datetime import date, timedelta
#
# ## 시작날짜와 종료날짜 설정
# start_date = date(2021, 1,1)
# end_date = date(2021,12,31)
# #
# ##
# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)
#
# for single_date in daterange(start_date, end_date):
#     a1 = (single_date.strftime("%Y-%m-%d"))
#
#     print(a1)

##
import urllib.request
from datetime import date, timedelta

start_date = date(2021, 1,1)
end_date = date(2021,12,31)

def daterange(start_date, end_date):
     for n in range(int((end_date - start_date).days)):
         yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
     a = (single_date.strftime("%Y-%m-%d"))



# imgURL = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1chlamday.geotif?chlorophyll%5B(2021-11-25T00:00:00Z)%5D%5B(-57.97917):(-66.68751)%5D%5B(-63.64583):(-54.9375)%5D&.draw=surface&.vars=longitude%7Clatitude%7Cchlorophyll&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff"


imgURL = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1chlamday.geotif?chlorophyll%5B(' + a + 'T00:00:00Z)%5D%5B(-57.97917):(-66.68751)%5D%5B(-63.64583):(-54.9375)%5D&.draw=surface&.vars=longitude%7Clatitude%7Cchlorophyll&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff"

urllib.request.urlretrieve(imgURL, f"E:/test/image{a}.tif")


## 필요 자료 설치
from datetime import date, timedelta
import urllib.request

## 시작날짜와 종료날짜 설정
start_date = date(2018, 7, 28) #시작일
end_date = date(2020, 8, 3) #종료일

## 다운로드 받을 폴더 설정
Download = 'D:/test/'


## 실행 코드
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
    url= 'https://seaice.uni-bremen.de/data/amsr2/asi_daygrid_swath/s3125/' + (single_date.strftime("%Y")) + '/' + (single_date.strftime("%b")).lower() + '/Antarctic3125/asi-AMSR2-s3125-' + (single_date.strftime("%Y%m%d")) + '-v5.4.tif'
    print(url)
    urllib.request.urlretrieve(url, 'D:/test/' + 'SIC_' + (single_date.strftime("%Y-%m-%d")) + '.tif')

