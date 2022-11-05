from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_coms as bc
import tok
import loging
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

app = ApplicationBuilder().token(tok.tok).build()

app.add_handler(CommandHandler("hi", bc.hi))
app.add_handler(CommandHandler("help", bc.help_t))
app.add_handler(CommandHandler("date", bc.time_date))

#app.add_handler(CommandHandler("hello", bc.cros()))

print('Server startup')

app.run_polling()