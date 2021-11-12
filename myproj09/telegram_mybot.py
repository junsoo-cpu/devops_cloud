import pprint
import telegram
import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요", file=sys.stderr)
    sys.exit(1)  # 종료 상태 값을 1로 지정하고, 프로그램 종료

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    # 대화방이 처음 열리면, 자동으로 호출되는 함수
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕 나는 junsoobot이야. 만나서 반가워"
    )

def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [
        tasks.get_current_lotto_numbers,
        tasks.ya,
        tasks.naver_search,
        tasks.time_check,
        tasks.remain_time_check,
        tasks.corona,
    ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
    else:
        response_text = "지원하지 않는 명령입니다."

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(
        Filters.text & (~Filters.command),
        echo,
    )

dispatcher.add_handler(echo_handler)

print("Started bot ...")

updater.start_polling()
updater.idle()

"""
이준수 과제 코드
"""
# def echo(update, context):
#     received_text: str = update.message.text
#
#     if tasks.time_check.check_available(received_text): # 시간 체크
#         response_text = tasks.time_check.time_check_response()
#     elif tasks.remain_time_check.last_check_available(received_text):   # 올해 남은 일 체크
#         response_text = (f"{tasks.remain_time_check.last_time_check_response()}일 남았습니다.")
#     elif tasks.corona.corona_check_available(received_text):    # 코로나 확진자 수
#         response_text = (f"금일 코로나 확진자 수는{tasks.corona.covid_num_crawling()}입니다.")
#     else:
#         response_text = "지원하지 않는 명령입니다."
#
#         context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text=response_text)
#
#         start_handler = CommandHandler("start", start)
#         dispatcher.add_handler(start_handler)
#
#         echo_handler = MessageHandler(
#             Filters.text & (~Filters.command),  # 명령이 아니고 text 라면 echo 호출
#             echo,
#         )
#         dispatcher.add_handler(echo_handler)
#         updater.idle()
#         updater.start_polling()

    # if tasks.ya.check_available(received_text):
    #     response_text = tasks. ya.make_response(received_text)
    # elif tasks.naver_search.check_available(received_text):
    #     response_text = tasks.naver_search.make_response(received_text)
    # else:
    #     response_text = "지원하지 않는 명령입니다."

    # if received_text == "야":
    #     reply_text = "왜?"
    # elif received_text.startswith("네이버 검색:"):
    #     query = received_text[7:]
    #     post_list = tasks.naver_search(query)
    #     # TODO : 응답 문자열 생성
    #     reply_text = ""
    #     for post in post_list:  # post를 사전으로 받아주었다.
    #         reply_text += post["title"] + "\n"  # post["title"]가 사전형식이기 때문에
    #
    #     for post in post_list:
    #         reply_text += post + "\n"     #post 문자열 형식으로 받기
    # else:
    #     reply_text = "지원하지 않는 명령입니다."
    #
    # reply_text = received_text

    # tasks.naver_search


# bot = telegram.Bot(token)

# 봇 정보 확인하기
# info = bot.getMe()
# pprint.pprint(info)

# resp = bot.getUpdates()
# pprint.pprint(resp)

# 봇에서 사용자에게 메시지 보내기
# chat_id = 2107171652
# bot.sendMessage(chat_id=chat_id, text="안녕 나는 봇이야")