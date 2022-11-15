import datetime
import subprocess
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, update
from aiogram import types
from tok import tok
import emoji
from aiogram.dispatcher.filters import Text
from loging import *
import random
import telebot




bot = Bot(tok)
dp = Dispatcher(bot)
print('Server startup')

item = {}
global gameIsStart
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]

CrossesOrToe = [emoji.emojize(':hollow_red_circle:'), emoji.emojize(':cross_mark:')]


#playerSymbol = CrossesOrToe[random.randint(0, 1)]


# botSymbol = ""
# if (playerSymbol == emoji.emojize(':hollow_red_circle:')):
#     botSymbol = emoji.emojize(':cross_mark:')
# else:
#     botSymbol = emoji.emojize(':hollow_red_circle:')

botSymbol = emoji.emojize(':cross_mark:')
playerSymbol = emoji.emojize(':hollow_red_circle:')


winbool = False
losebool = False



def clear():  # await ?
    global gameGround
    gameGround = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]
def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        global losebool
        losebool = True

# def defend(cell_1, cell_2, posDef):
#     if cell_1 == playerSymbol and cell_2 == playerSymbol:
#         posDef = botSymbol



@dp.message_handler(commands=['go'])
async def send_welcome(message: types.Message):
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.row_width = 2
    bt = [emoji.emojize(':red_question_mark:help'), emoji.emojize(':alarm_clock:time'), emoji.emojize(':video_game:play'), emoji.emojize(':mobile_phone:calc')]
    keybord.add(*bt)
    await message.reply(f"Привет! {message.from_user.full_name} Я новый бот. \nМои команды это кнопочки снизу.\nС чего начнем?" , reply_markup=keybord)
    await log_g2(message)

@dp.message_handler(Text(equals = [emoji.emojize(':red_question_mark:help')]))
async def c_help(message: types.Message):
    await message.reply(emoji.emojize(':red_question_mark:help - справка по командам\n:alarm_clock:time - текущее время\n:video_game:play - играем в крестики & нолики\n:mobile_phone:calc - калькулируем'))
    await log_g2(message)

@dp.message_handler(Text(equals = [emoji.emojize(':mobile_phone:calc')]))
async def c_help(message: types.Message):
    await message.reply(emoji.emojize('ааа, мы хотим посчитать :man_technologist:'))

    await log_g2(message)

@dp.message_handler(Text(equals = [emoji.emojize(':alarm_clock:time')]))
async def c_time(message: types.Message):
    now = datetime.datetime.now()
    curr = now.strftime("%H:%M:%S")
    await message.reply(emoji.emojize(f':alarm_clock: - текущее время - {curr}'))
    await log_g2(message)

@dp.message_handler(Text(equals = [emoji.emojize(':video_game:play')]))
async def c_play(message: types.Message):

    # keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keybord.row_width = 3
    # bt = ['1','2','3','4','5','6','7','8','9']
    # keybord.add(*bt)
    await message.reply(f"Ну что {message.from_user.full_name} сыграем!\n Твой ход!")   # , reply_markup=keybord)

    #await bot.send_message(message.chat.id, "Игра началась")
    global gameIsStart
    clear()
    gameIsStart = True

    if gameIsStart == True:
        item = {}
        global markup
        markup = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)

        i = 0

        for i in range(9):
            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        await bot.send_message(message.chat.id, emoji.emojize(':cross_mark:   Выбери клетку   :hollow_red_circle:'),
                               reply_markup=markup)
        await log_g2(message)


@dp.callback_query_handler(lambda call: True)
async def callbackInline(call):
    if (call.message):

        for i in range(9):
            if call.data == str(i):
                print(i)
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol

        for i in range(9):
            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))
        global markup
        markup = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)

        win(gameGround[0], gameGround[1], gameGround[2])
        win(gameGround[3], gameGround[4], gameGround[5])
        win(gameGround[6], gameGround[7], gameGround[8])
        win(gameGround[0], gameGround[3], gameGround[6])
        win(gameGround[1], gameGround[4], gameGround[7])
        win(gameGround[2], gameGround[5], gameGround[8])
        win(gameGround[0], gameGround[4], gameGround[8])
        win(gameGround[2], gameGround[4], gameGround[6])

        lose(gameGround[0], gameGround[1], gameGround[2])
        lose(gameGround[3], gameGround[4], gameGround[5])
        lose(gameGround[6], gameGround[7], gameGround[8])
        lose(gameGround[0], gameGround[3], gameGround[6])
        lose(gameGround[1], gameGround[4], gameGround[7])
        lose(gameGround[2], gameGround[5], gameGround[8])
        lose(gameGround[0], gameGround[4], gameGround[8])
        lose(gameGround[2], gameGround[4], gameGround[6])

        global winbool
        global gameIsStart
        if winbool:
            clear()
            await bot.send_message(call.message.chat.id, emoji.emojize(' Я проиграл :loudly_crying_face:'))
            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            await bot.send_message(call.message.chat.id,
                                   emoji.emojize(' Я победил!!! :winking_face_with_tongue::victory_hand:'))
            losebool = False
            gameIsStart = False



# @dp.message_handler()                             - эхо
# async def echo(message: types.Message):
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) #or True для пропуска обновлений