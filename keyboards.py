from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://cattish.ru/breed/')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://lapkins.ru/dog/')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
