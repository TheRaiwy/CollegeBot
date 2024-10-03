from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_command(message: types.Message):
    button = InlineKeyboardButton("Открыть приложение", url="https://t.me/umniygorodMogilev_bot/app")
    keyboard = InlineKeyboardMarkup().add(button)

    await message.reply("Добро пожаловать в умный город Могилев! Здесь вы можете получить быстродоступную информацию по инфраструктуре.", reply_markup=keyboard)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
