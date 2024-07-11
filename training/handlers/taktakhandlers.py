from aiogram import Router, F
from aiogram.filters import CommandStart
from keyboards.creat_inlinekb import creat_inlinekb
from aiogram.types import Message, CallbackQuery


router= Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = creat_inlinekb(1, 'платежи', 'заказы')
    await message.answer(
        text='Выберите что будем настраивать',
        reply_markup=keyboard
    )

@router.callback_query(F.data == "платежи")
async def send_random_value(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, 'просроченные', 'сегодня', 'на этой неделе', 'в этом месяце', last_btn='подтвердить')
    await callback.message.answer(
        text='Какой период',
        reply_markup=keyboard
    )
    await callback.answer()

@router.callback_query(F.data == "заказы")
async def send_random_value(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, 'просроченные', 'сегодня', 'на этой неделе', 'в этом месяце', last_btn='подтвердить')
    await callback.message.answer(
        text='Какой период',
        reply_markup=keyboard
    )



    await callback.answer()
