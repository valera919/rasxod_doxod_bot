from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton



def generate_main_keyboards():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btns = [KeyboardButton(text="Доходы"), KeyboardButton(text="Расходы")]
    markup.add(*btns)
    return markup

def show_add_rasxodi():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btns = [KeyboardButton(text="Добавить расходы"), KeyboardButton(text="Показать расходы")]
    markup.add(*btns)
    return markup

def show_add_doxodi():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btns = [KeyboardButton(text="Добавить доходы"), KeyboardButton(text="Показать доходы")]
    markup.add(*btns)
    return markup


