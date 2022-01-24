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
# import urllib.request
# from da
# start_date = date(2021, 1,1)
# end_date = datetime import date, timedelta
# te(2021,12,31)
#
# def daterange(start_date, end_date):
#      for n in range(int((end_date - start_date).days)):
#          yield start_date + timedelta(n)
#
# for single_date in daterange(start_date, end_date):
#      a = (single_date.strftime("%Y-%m-%d"))
#
#
#
# # imgURL = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1chlamday.geotif?chlorophyll%5B(2021-11-25T00:00:00Z)%5D%5B(-57.97917):(-66.68751)%5D%5B(-63.64583):(-54.9375)%5D&.draw=surface&.vars=longitude%7Clatitude%7Cchlorophyll&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff"
#
#
# imgURL = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/erdMH1chlamday.geotif?chlorophyll%5B(' + a + 'T00:00:00Z)%5D%5B(-57.97917):(-66.68751)%5D%5B(-63.64583):(-54.9375)%5D&.draw=surface&.vars=longitude%7Clatitude%7Cchlorophyll&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff"
#
# urllib.request.urlretrieve(imgURL, f"E:/test/image{a}.tif")


## 날짜 및 위도 경도 설정 추가
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

# 파일복사 프로그램 ex)
# 모듈
import sys
import os

# 상수
FILENAME = 'mycopy.py'
OPTION = '-cp'

# 예외처리를 직접 만들기 위한 클래스
class FileTypeError(Exception):
    pass

# 예외 처리 구문
try:
    # sys.argv = ['mycopy', '-cp', '복사할 txt파일', '붙여넣을 txt파일']
    # sys.argv의 원소를 각각 변수로 초기화 하는 과정에서 리스트에 누락이 있으면, IndexError 발생
    option = sys.argv[1] # 옵션
    f_copy = sys.argv[2] # 복사할 파일
    f_paste = sys.argv[3] # 붙여넣을 파일

    if option == OPTION: # 옵션이 정확히 들어왔을 경우
        if f_copy[-4:] == '.txt' and f_paste[-4:] == '.txt':
        # 복사/붙여넣을 파일의 형식이 .txt인 경우
            with open(f_copy, 'rt', encoding="utf-8") as f:
                text = f.read() # 복사할 파일을 읽어 텍스트를 변수로 저장
            with open(f_paste, 'wt', encoding="utf-8") as f:
                f.write(text)# 붙여넣을 파일을 열어 텍스트 복사

            # 파일 복사 완료 후 내용 출력여부 확인
            answer = input('파일 복사가 완료되었습니다. 복사한 파일의 내용을 확인하시겠습니까?(Y/N) : ')
            if answer == 'Y' or answer == 'y' or answer == 'ㅛ': # Y
                print('파일명) {}' .format(f_paste))
                print('내용)')
                with open(f_paste, 'rt', encoding="utf-8") as f:
                    read = f.read() # 파일을 열어 저장된 내용 출력
                print(read)
            else: # N
                print('파일 복사 프로그램을 종료합니다.') # 프로그램 종료

        else: # 복사/붙여넣을 파일의 형식이 .txt가 아닌 경우
            raise FileTypeError() # 직접 생성한 파일형식에러 강제 발생

    else: # 옵션이 정확하게 들어오지 않았을 경우
        raise IndexError # IndexError 강제 발생

# 에러 처리 구문
except IndexError: # sys.argv 리스트에 값이 하나라도 누락되었을 경우 에러 발생
    print('커맨드 형식이 올바르지 않습니다. 아래 형식을 참조하여 다시 입력하세요.')
    print('커맨드 형식 : python {0} {1} [복사할 txt파일] [붙여넣을 txt파일]' .format(FILENAME, OPTION))

except (FileTypeError, FileNotFoundError): # txt파일이 아니거나 복사할 파일이 없는 경우
    print('txt파일이 없거나 파일의 형식이 올바르지 않습니다.')
    print('현재 경로에 있는 \'*.txt\' 파일 목록은 아래와 같습니다.')
    print('-----------------------------------------------------')

    # OS별 현재 경로의 .txt 파일 리스트 출력
    if os.name == 'nt': # Window OS
        os.system('dir /b | findstr .txt')
    else: # Linux OS, Mac OS
        os.system('ls | grep .txt')
