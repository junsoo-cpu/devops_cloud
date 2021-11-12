"""
현재 시간
"""
import datetime

def check_available(received_text: str) -> bool:    # 함수의 인자와 리턴 값 타입을 명시
    return received_text.startswith("몇시야")

def time_check_response():
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y년 %m월 %d일 %H시 %M분 입니다.")
    return nowDate