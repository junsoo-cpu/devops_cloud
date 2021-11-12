# 웹 크롤링 프로젝트
# https://sodayeong.tistory.com
from datetime import date

end_date = input().split()
start_date = input().split()

end = date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
start = date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
resl = (end - start).days
