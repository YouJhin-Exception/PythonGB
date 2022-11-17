from aiogram.types import CallbackQuery

from tok import tok
import emoji
from loging import *
import random

bot = Bot(tok)
dp = Dispatcher(bot)
print('Server startup')

item = {}

gameIsStart = False
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]
botSymbol = emoji.emojize(':cross_mark:')
playerSymbol = emoji.emojize(':hollow_red_circle:')
#playerSymbol = CrossesOrToe[random.randint(0, 1)]

# botSymbol = ""
# if (playerSymbol == emoji.emojize(':hollow_red_circle:')):
#     botSymbol = emoji.emojize(':cross_mark:')
# else:
#     botSymbol = emoji.emojize(':hollow_red_circle:')

# def defend(cell_1, cell_2, posDef):
#     if cell_1 == playerSymbol and cell_2 == playerSymbol:
#         posDef = botSymbol

winbool = False
losebool = False

calc_mark = types.InlineKeyboardMarkup(resize_keyboard=True)
calc_mark.row(types.InlineKeyboardButton("CE", callback_data="CE"),
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

calc_mark.row(types.InlineKeyboardButton("j", callback_data="j"),
              types.InlineKeyboardButton("0", callback_data="0"),
              types.InlineKeyboardButton(",", callback_data="."),
              types.InlineKeyboardButton("=", callback_data="="))

calc_mark.row(types.InlineKeyboardButton("(", callback_data="("),
              types.InlineKeyboardButton(")", callback_data=")"))


value = ''
oldvalue = ''

typeS = None

def clear():
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

@dp.message_handler(Text(equals = [emoji.emojize(':alarm_clock:time')]))
async def c_time(message: types.Message):
    now = datetime.datetime.now()
    curr = now.strftime("%H:%M:%S")
    await message.reply(emoji.emojize(f':alarm_clock: - текущее время - {curr}'))
    await log_g2(message)


@dp.message_handler(Text(equals=[emoji.emojize(':video_game:play')]))
async def c_play(message: types.Message):
    global gameIsStart
    clear()
    gameIsStart = True

    if gameIsStart == True:
        i = 0
        item = {}
        global game_mark
        game_mark = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
        # item[0] = types.InlineKeyboardButton(gameGround[0], callback_data="cell0")
        # item[1] = types.InlineKeyboardButton(gameGround[0], callback_data="cell1")
        # item[2] = types.InlineKeyboardButton(gameGround[0], callback_data="cell2")
        # item[3] = types.InlineKeyboardButton(gameGround[0], callback_data="cell3")
        # item[4] = types.InlineKeyboardButton(gameGround[0], callback_data="cell4")
        # item[5] = types.InlineKeyboardButton(gameGround[0], callback_data="cell5")
        # item[6] = types.InlineKeyboardButton(gameGround[0], callback_data="cell6")
        # item[7] = types.InlineKeyboardButton(gameGround[0], callback_data="cell7" + str(i))

        i = 0

        for i in range(9):
            item[i] = types.InlineKeyboardButton(gameGround[0], callback_data="cell" + str(i))

        game_mark.row(item[0], item[1], item[2])
        game_mark.row(item[3], item[4], item[5])
        game_mark.row(item[6], item[7], item[8])
        await bot.send_message(message.chat.id, emoji.emojize(':cross_mark:   Выбери клетку   :hollow_red_circle:'),
                               reply_markup=game_mark)
        global typeS
        typeS = "game"
        await log_g2(message)


@dp.message_handler(Text(equals = [emoji.emojize(':mobile_phone:calc')]))
async def new_calc(message: types.Message):
    # await message.reply(emoji.emojize('ааа, мы хотим посчитать :man_technologist:'))
    # calc_chose_mark = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    # calc_chose_mark.row(types.InlineKeyboardButton('рациональные', callback_data="ratio"),
    #                     types.InlineKeyboardButton('комплексные', callback_data="compl"))
    # await bot.send_message(message.chat.id, emoji.emojize('Для начала выбери с камими числами будем работать'),
    #                        reply_markup=calc_mark)

    global value
    if value == '':
        await bot.send_message(message.chat.id, '0', reply_markup=calc_mark)
    else:
        await bot.send_message(message.chat.id, value, reply_markup=calc_mark)
    global typeS
    typeS = "calc"
    await log_g2(message)


@dp.callback_query_handler()
async def callbackInline(call):
    print(typeS)
    if typeS == "game":
        for i in range(9):
            if call.data == "cell" + str(i):
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
                    item[i] = types.InlineKeyboardButton(gameGround[i], callback_data="cell" + str(i))
                global markup
                markup = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
                markup.row(item[0], item[1], item[2])
                markup.row(item[3], item[4], item[5])
                markup.row(item[6], item[7], item[8])
                await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                                    reply_markup=markup)

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


    elif typeS == "calc":
        global value, oldvalue
        data = call.data

        if data == 'no':
            pass
        elif data == 'C':
            value = ''
        elif data == 'CE':
            value = 'заглушка'
        elif data == "<=":
            if value != "":
                value = value[:len(value) - 1]
        elif data == '=':
            try:
                value = str(eval(value))
            except:
                value = "делишь на 0, серьезно?!"
        else:
            value += data
        if (value != oldvalue and value != '') or ('0' != oldvalue and value == ''):
            if value == '':
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            text='0', reply_markup=calc_mark)
                oldvalue = '0'
            else:
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            text=value,
                                            reply_markup=calc_mark)
                oldvalue = value

        if value == "делишь на 0, серьезно?!":
            value = ''




# @dp.message_handler()                             - эхо
# async def echo(message: types.Message):
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) #or True для пропуска обновлений