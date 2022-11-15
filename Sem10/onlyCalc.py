import emoji
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from Sem10.tok import tok

bot = Bot(tok)
dp = Dispatcher(bot)


@dp.message_handler(commands=['go'])
async def send_welcome(message: types.Message):
    keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keybord.row_width = 2
    bt = [emoji.emojize(':red_question_mark:help'), emoji.emojize(':alarm_clock:time'), emoji.emojize(':video_game:play'), emoji.emojize(':mobile_phone:calc')]
    keybord.add(*bt)
    await message.reply(f"Привет! {message.from_user.full_name} Я новый бот. \nМои команды это кнопочки снизу.\nС чего начнем?" , reply_markup=keybord)


@dp.message_handler(Text(equals = [emoji.emojize(':red_question_mark:help')]))
async def c_help(message: types.Message):
    await message.reply(emoji.emojize(':red_question_mark:help - справка по командам\n:alarm_clock:time - текущее время\n:video_game:play - играем в крестики & нолики\n:mobile_phone:calc - калькулируем'))

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

value = ''
oldvalue = ''




@dp.message_handler(Text(equals = [emoji.emojize(':mobile_phone:calc')]))
async def new_calc(message: types.Message):
    global gameIsStart
    gameIsStart = False
    if gameIsStart == False:
        # await message.reply(emoji.emojize('ааа, мы хотим посчитать :man_technologist:'))
        # calc_chose_mark = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
        # calc_chose_mark.row(types.InlineKeyboardButton('рациональные', callback_data="ratio"),
        #                     types.InlineKeyboardButton('комплексные', callback_data="compl"))
        # await bot.send_message(message.chat.id, emoji.emojize('Для начала выбери с камими числами будем работать'),
        #                        reply_markup=calc_mark)
        global value
        if value =='':
            await bot.send_message(message.chat.id, '0', reply_markup=calc_mark)
        else:
            await bot.send_message(message.chat.id, value, reply_markup=calc_mark)



@dp.callback_query_handler(lambda call: call)
async def callbackCalc(call):
    global value, oldvalue
    data = call.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '=':
        value = str(eval(value))
    else:
        value += data
    if value != oldvalue:
        if value =='':
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='0',reply_markup=calc_mark)
        else:
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=value,
                                  reply_markup=calc_mark)

    oldvalue=value

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) #or True для пропуска обновлений