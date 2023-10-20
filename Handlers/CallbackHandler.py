from Loader import bot, dp
import Config as Cfg
from aiogram import types

__all__ = ['dp']


@dp.callback_query_handler(text = "start")
async def startCall(call: types.CallbackQuery):
    await call.answer("Start callback")