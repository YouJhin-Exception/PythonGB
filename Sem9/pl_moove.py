




async def pl_m():
    for i in range(9):
        if call.data == str(i):
            print(i)
            if (gameGround[i] == " "):
                gameGround[i] = playerSymbol
        item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

    global markup
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.row(item[0], item[1], item[2])
    markup.row(item[3], item[4], item[5])
    markup.row(item[6], item[7], item[8])
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)