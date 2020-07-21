from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandStart())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))
