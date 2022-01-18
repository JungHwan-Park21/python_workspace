# data = list(range(1, 46))
#
# import random
#
#
# def random_pop(data):
#     number = random.randint(0, len(data) - 1)
#     return data.pop(number)
#
#
# for i in range(1, 7):
#     print(random_pop(data))

##
# import webbrowser
#
# url = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1chlamday.geotif?chlorophyll%5B(2021-11-16T00:00:00Z)%5D%5B(-57.97917):(-66.68751)%5D%5B(-63.64583):(-54.9375)%5D&.draw=surface&.vars=longitude%7Clatitude%7Cchlorophyll&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff"
#
# # urllib.request.urlretrieve(imgURL, "E:/test/image1.tif")
#
# webbrowser.open(url)
#
# import webbrowser
#
# url = "https://www.naver.com"
#
# webbrowser.open(url)

## 날짜반복
from datetime import date, timedelta

## 시작날짜와 종료날짜 설정
start_date = date(2021, 1,1)
end_date = date(2021,12,31)

##
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
    a = (single_date.strftime("%Y-%m-%d"))

print(a)