import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5553326894:AAEbX9Xcu5318Jaw2EjmZC2Z72ITcNccsjc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer("*В дверь постучали 0.5 раз*\nКарлик - подумал Штирлиц.\n*В дверь постучали 1 раз*\nДва карлика - подумал Штирлиц")
    await message.answer_photo(types.ImputFile('5167025a5117df9212a9e9a10c108ff7.jpeg'))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)