import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться на теннис')],
    [KeyboardButton(text='Расписание занятий')],
    [KeyboardButton(text='Контакты'),
        KeyboardButton(text='О нас')]])

bot = Bot(token='8282810126:AAEXC4txcY0HYNO-x-Q5jKuFbsVCrzHEB8w')

dp = Dispatcher()

async def main():
    await dp.start_polling(bot)
    
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Как тебя зовут?', reply_markup=main_keyboard)
    await message.reply('Вау!!!')
    
@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply('Щас я тебе помогу. Не переживай!')
    
@dp.message(F.text == 'У меня все хорошо')
async def nice(message: Message):
    await message.answer('Ну и супер.')
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен.')
