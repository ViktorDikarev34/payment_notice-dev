import asyncio
import logging
import operator
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import Command
from config_reader import config
from aiogram import html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.formatting import Text, Bold
from aiogram_dialog.widgets.kbd import Multiselect
from aiogram_dialog.widgets.text import Format



#Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML)
    )

# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

#хэндлер на запуск
# На нажатие кнопки старт выдает приветственное сообщение и кнопку "настройки"
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    content = Text(
        'Здравствуйте, ',
        Bold(message.from_user.full_name),
        ', нажмите кнопку "настройки"'
    )
    kb = [
        [
            types.KeyboardButton(text="Настройки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Нажмите кнопку "настройки" для выбора настроек'
    )
    await message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )


@dp.message(F.text.lower() == "настройки")
async def options(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Статусы платежей"),
            types.KeyboardButton(text="Статусы заказов")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите что вы хотите настроить"
    )
    await message.answer("Что именно будем настраивать?", reply_markup=keyboard)



if __name__ == "__main__":
    asyncio.run(main())
