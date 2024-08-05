from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config_data.config import Config, load_config
from handlers import taktakhandlers
from config_data.config import token_ms



config: Config = load_config('.env')

bot_token = config.tg_bot.token

dp = Dispatcher()
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp.include_router(taktakhandlers.router)

if __name__ == '__main__':
    dp.run_polling(bot)