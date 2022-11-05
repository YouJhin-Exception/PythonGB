from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from loging import *


async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_g(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def time_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_g(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().date()}\n{datetime.datetime.now().time()}')

async def help_t(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_g(update, context)
    await update.message.reply_text(f'/hi\n/date\n/help\n/cross')

# async def cross(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')