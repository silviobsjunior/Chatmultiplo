import re
import sys

from pymongo import MongoClient
from telebot import types

import db
import apicorreios as correios
import apitrackingmore as trackingmore

def check_type(code):
    s10 = (r"^[A-Za-z]{2}\d{9}[A-Za-z]{2}$")
    ali = (r"^([A-Za-z]{2}\d{14}|(1Z)[0-9A-Z]{16}|[A-Za-z]{2}\d{12}[A-Za-z]{3}|\d{12}|\d{22}|[A-Za-z]{2}\d{18}|[A-Za-z]{1}\d{12}[A-Za-z]{3}|[A-Za-z]{2}\d{13}|[A-Za-z]{4}\d{9}|\d{10}|[A-Za-z]{5}\d{10}[A-Za-z]{2})$")

    if re.search(s10, str(code)):
        print('correios')
        return correios
    elif re.search(ali, str(code)):
        print('trackingmore')
        return trackingmore
    else:
        print('none')
        return None


def send_clean_msg(bot, id, txt):
    markup_clean = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(id, txt, parse_mode='HTML', reply_markup=markup_clean)


def check_package(code):
    cursor = db.search_package(code)
    if cursor:
        return True
    return False

def check_update(code, max_retries=3):
    api_type = check_type(code)
    if api_type is trackingmore:
        return trackingmore.get(code, max_retries)
    elif api_type is correios:
        return correios.get(code, max_retries)
    else:
        return status.TYPO


async def async_check_update(code, max_retries=3):
    api_type = check_type(code)
    if api_type is trackingmore:
        return status.TYPO
        return trackingmore.get(code, max_retries)
    elif api_type is correios:
        return await correios.async_get(code, max_retries)
    else:
        return status.TYPO


if __name__ == '__main__':
   print(check_update(sys.argv[1], 1))
