import asyncio
import logging
from random import randint
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from aiogram.filters import Command, BaseFilter
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import html, F
from magic_filter import F
from config_reader import config
import requests
import time
from aiogram.types import Message
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest


#Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties( # type: ignore
        parse_mode=ParseMode.HTML) # type: ignore
    )

# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

admins_id: list[int] = [1323008818]

class IsAdmin(BaseFilter):
    def __init__(self, admins_id: list[int]) -> None:
        self.admins_id = admins_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_id

@dp.message(IsAdmin(admins_id))
async def answer_if_admins_update(message: Message):
    await message.answer(text='You Admin')

@dp.message()
async def answer_if_not_admins_id(message: Message):
    await message.answer(text='You loser')


if __name__ == "__main__":
    asyncio.run(main())
