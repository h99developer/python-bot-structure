from aiogram import types, executor, Dispatcher, Bot
import Config as cfg

bot = Bot(cfg.BOT_TOKEN)
dp = Dispatcher(bot)



if __name__ == "__main__":

    from Handlers.MessageHandler import dp
    from Handlers.CallbackHandler import dp

    executor.start_polling(dp)