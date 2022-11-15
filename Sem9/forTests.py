@dp.callback_query_handler(lambda call: True)
async def callbackInline(call):
    if (call.message):

        # bot manager
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol

        for i in range(9):
            if call.data == str(i):
                print(i)
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol

            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

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

        # update cells
        global markup
        markup = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)

        global winbool
        global gameIsStart
        if winbool:
            clear()
            await bot.send_message(call.message.chat.id, "Я проиграл :(")
            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            await bot.send_message(call.message.chat.id, "Я выиграл!!")

            losebool = False
            gameIsStart = False