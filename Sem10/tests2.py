import datetime
import subprocess
from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, update
from aiogram import types

from Sem10.testSSS import dp
from Sem9 import tok
import emoji
from aiogram.dispatcher.filters import Text
from loging import *
import random
import telebot



bot = Bot(tok.tok)
dp = Dispatcher(bot)



@dp.message_handler(Text(equals = [emoji.emojize(':mobile_phone:calc')]))
async def new_calc(message: types.Message):
    await message.reply(emoji.emojize('ааа, мы хотим посчитать :man_technologist:'))
    calc_chose_mark = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    calc_chose_mark.row(types.InlineKeyboardButton('рациональные', callback_data="ratio"), types.InlineKeyboardButton('комплексные', callback_data="compl"))
    await bot.send_message(message.chat.id, emoji.emojize('Для начала выбери с камими числами будем работать'),
                           reply_markup=calc_chose_mark)

@dp.callback_query_handler(text="ratio")
async def ra_calc(callback: types.CallbackQuery):
    await callback.message.answer('Вас понял - рациональные')
    calc_mark = types.InlineKeyboardMarkup()
    calc_mark.row(types.InlineKeyboardButton("CE", callback_data="no"),
                  types.InlineKeyboardButton("C", callback_data="C"),
                  types.InlineKeyboardButton("<=", callback_data="<="),
                  types.InlineKeyboardButton("/", callback_data="/"))

    calc_mark.row(types.InlineKeyboardButton("7", callback_data="7"),
                  types.InlineKeyboardButton("8", callback_data="8"),
                  types.InlineKeyboardButton("9", callback_data="9"),
                  types.InlineKeyboardButton("*", callback_data="*"))

    calc_mark.row(types.InlineKeyboardButton("4", callback_data="4"),
                  types.InlineKeyboardButton("5", callback_data="5"),
                  types.InlineKeyboardButton("6", callback_data="6"),
                  types.InlineKeyboardButton("-", callback_data="-"))

    calc_mark.row(types.InlineKeyboardButton("1", callback_data="1"),
                  types.InlineKeyboardButton("2", callback_data="2"),
                  types.InlineKeyboardButton("3", callback_data="3"),
                  types.InlineKeyboardButton("+", callback_data="+"))

    calc_mark.row(types.InlineKeyboardButton(" ", callback_data="no"),
                  types.InlineKeyboardButton("0", callback_data="0"),
                  types.InlineKeyboardButton(",", callback_data="."),
                  types.InlineKeyboardButton("=", callback_data="="))
    await callback.message.answer('Вот тебе кнопки', reply_markup=calc_mark)



# @dp.callback_query_handler(text="ratio")
# async def ra_calc(callback: types.CallbackQuery):
#     await callback.message.answer('Вас понял - рациональные')
#     calc_mark = types.InlineKeyboardMarkup()
#     calc_mark.row(types.InlineKeyboardButton("CE", callback_data="no"),
#                   types.InlineKeyboardButton("C", callback_data="C"),
#                   types.InlineKeyboardButton("<=", callback_data="<="),
#                   types.InlineKeyboardButton("/", callback_data="/"))
#
#     calc_mark.row(types.InlineKeyboardButton("7", callback_data="7"),
#                   types.InlineKeyboardButton("8", callback_data="8"),
#                   types.InlineKeyboardButton("9", callback_data="9"),
#                   types.InlineKeyboardButton("*", callback_data="*"))
#
#     calc_mark.row(types.InlineKeyboardButton("4", callback_data="4"),
#                   types.InlineKeyboardButton("5", callback_data="5"),
#                   types.InlineKeyboardButton("6", callback_data="6"),
#                   types.InlineKeyboardButton("-", callback_data="-"))
#
#     calc_mark.row(types.InlineKeyboardButton("1", callback_data="1"),
#                   types.InlineKeyboardButton("2", callback_data="2"),
#                   types.InlineKeyboardButton("3", callback_data="3"),
#                   types.InlineKeyboardButton("+", callback_data="+"))
#
#     calc_mark.row(types.InlineKeyboardButton(" ", callback_data="no"),
#                   types.InlineKeyboardButton("0", callback_data="0"),
#                   types.InlineKeyboardButton(",", callback_data="."),
#                   types.InlineKeyboardButton("=", callback_data="="))
#     await callback.message.answer('Вот тебе кнопки', reply_markup=calc_mark)