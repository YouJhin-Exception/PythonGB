from aiogram.types import message
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types

async def log_g(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log_file = open('log.txt', 'a', encoding='UTF-8')
    # log_file.write(f'{update.effective_user.id}, {update.effective_user.first_name}, {update.message.text}, {datetime.datetime.now().time()}\n')
    # log_file.close()

    with open('log2.csv', 'a', encoding='UTF-8') as f1:
        f1.write(f'{update.effective_user.id}, {update.effective_user.first_name}, {update.message.text}, {datetime.datetime.now().time()}\n')
        #f1.close()

async def log_g2(message):
    with open('log2.csv', 'a', encoding='UTF-8') as f1:
        now = datetime.datetime.now()
        date = now.date()
        curr = now.strftime("%H:%M:%S")
        f1.write(f'ID - {message.from_user.id}, Имя пользователя - {message.from_user.full_name}, Текст сообщения -{[message.text]}, Дата и время сообщения - {date}  -  {curr}\n')
