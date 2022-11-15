import random

import emoji
from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher.filters import Text

from Sem10.tok import tok

bot = Bot(tok)
dp = Dispatcher(bot)





item = {}
global gameIsStart
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]
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

@dp.message_handler(Text(equals = [emoji.emojize(':video_game:play')]))
async def c_play(message: types.Message):
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