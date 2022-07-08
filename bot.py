from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from tools import DBTools
from keyboards import generate_main_keyboards, show_add_rasxodi
import datetime



bot = Bot("")
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    await bot.send_message(chat_id, f"Ну здравствуй {full_name}", reply_markup=generate_main_keyboards())
    await register_user(message)


async def register_user(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    DBTools().user_tool.register_user(full_name, chat_id)



@dp.message_handler(lambda message: message.text=="Расходы")
async def rasxodi_handler(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Выберите категорию: ", reply_markup=show_add_rasxodi())



@dp.message_handler(lambda message: message.text=="Добавить расходы")
async def show_rasxodi(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Введите название расхода в формате (расход цена. Пример: хлеб 2800): ")


@dp.message_handler()
async def add_rasxod_to_db(message: Message):
    chat_id = message.chat.id
    text_message = message.text.split(" ")
    user_id = DBTools().user_tool.get_user_id(chat_id)
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    product_name = text_message[0]
    price = int(text_message[1])
    DBTools().user_tool.add_rasxod_to_db(user_id, product_name, price, date)
    await bot.send_message(chat_id, "Напишите название категории расхода: ")







executor.start_polling(dp, skip_updates=True)