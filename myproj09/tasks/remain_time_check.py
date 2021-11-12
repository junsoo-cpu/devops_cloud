"""
올해 남은 일 수
"""
import datetime

def last_check_available(received_text: str) -> bool:    # 함수의 인자와 리턴 값 타입을 명시
    return received_text.startswith("올해 얼마나 남았어?")

def last_time_check_response():
    last_day = datetime.datetime(2021,12,31)
    now_day = datetime.datetime.now()
    remain_time = last_day - now_day
    return remain_time.days