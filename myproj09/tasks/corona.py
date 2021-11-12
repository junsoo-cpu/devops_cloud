"""
코로나 확진자 수
"""
from bs4 import BeautifulSoup
import urllib.request as req

def check_available(received_text: str) -> bool:    # 함수의 인자와 리턴 값 타입을 명시
    return received_text.startswith("코로나현황")

def make_response(received_text: str) -> str:
    code = req.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%95%EC%A7%84%EC%9E%90")
    soup = BeautifulSoup(code, "html.parser")
    covid_num = soup.select("div.status_info em")
    result = f"금일 코로나 확진자 수는{covid_num[0].string}명 입니다." #=> 확진자
    return result

