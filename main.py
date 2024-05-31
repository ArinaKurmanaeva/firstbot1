from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboards import get_keyboard_1
from database.database import initialize_db, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет', reply_markup= get_keyboard_1())
    else:
        await message.answer('Привет', reply_markup= get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://vetson.ru/upload/iblock/1bd/c73x437pcxc6afyjij70rduo6rw7g0rh.png', caption= 'Вот тебе кот!')
@dp.message_handler(lambda message: message.text == 'перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('тут ты можешь попросить бота отправить фото собаки')

@dp.message_handler(lambda message: message.text == 'отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://e7.pngegg.com/pngimages/472/36/png-clipart-puppy-pet-dog-lazy-dog.png', caption= 'Вот тебе собака!')

@dp.message_handler(lambda message: message.text == 'вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('тут ты можешь попросить ,бота отправить фото кота', reply_markup= get_keyboard_1())


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command = '/start', description = 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command = '/help', description = 'Команда для того, чтобы узнать, с чем может помочь бот'),
        types.BotCommand(command ='/product', description ='Каталог товаров'),
    ]
    await bot.set_my_commands(commands)


@dp. message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с...')

@dp. message_handler(commands= 'product')
async def product(message: types.Message):
    await message.reply('У нас есть...')

@dp. message_handler()
async def echo(message:types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)

