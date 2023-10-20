from Loader import bot, dp
import Config as Cfg
from aiogram import types


__all__ = ['dp']


@dp.message_handler(commands = ['start'])
async def startCommand(message: types.Message):
    await message.reply("Start command")