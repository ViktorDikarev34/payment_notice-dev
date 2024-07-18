from aiogram import Router, F
from aiogram.filters import CommandStart
from keyboards.creat_inlinekb import creat_inlinekb
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON



router= Router()

user_data={}

#При старте выдает две кнопки - платежи и заказы
@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = creat_inlinekb(1, LEXICON['but_1'], LEXICON['but_2'])
    await message.answer(
        text='Выберите что будем настраивать',
        reply_markup=keyboard
    )

spisok_tipo_ms = ['новый', 'не оплачено', 'оплачено']

#При нажатии платежи выдает следующее сообщение "какой статус" и кнопки из списка, можно выбирать несколько
@router.callback_query(F.data == LEXICON['but_1'])
async def send_random_value_payment(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, *spisok_tipo_ms, last_btn=LEXICON['but_4'])
    user_data.setdefault('item_type', callback.data)
    await callback.message.edit_text( # type: ignore
        text='Какой статус',
        reply_markup=keyboard
    )
    await callback.answer()

#При нажатии заказы выдает следующее сообщение "какой статус" и кнопки из списка, можно выбирать несколько
@router.callback_query(F.data == LEXICON['but_2'])
async def send_random_value_orders(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, *spisok_tipo_ms, last_btn=LEXICON['but_4'])
    user_data.setdefault('item_type', callback.data)
    await callback.message.edit_text(  # type: ignore
        text='Какой статус',
        reply_markup=keyboard
    )
    await callback.answer()

#Набор статусов
@router.callback_query(F.data.in_(spisok_tipo_ms))
async def send_random_value(callback: CallbackQuery):
    user_data.setdefault('status', set())
    user_data['status'].add(callback.data)
    await callback.answer(
        text=f'Вы выбрали {callback.data}'
    )

#При нажатии кнопки подтвердить выдает сообщение с кнопками периода
@router.callback_query(F.data == 'last_btn')
async def press_and_assembly(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, LEXICON['but_5'], LEXICON['but_6'], LEXICON['but_7'], LEXICON['but_8'])
    user_data['status'] = list(user_data['status'])
    await callback.message.edit_text( # type: ignore
        text = 'За какой период',
        reply_markup=keyboard
    )
    await callback.answer()

#При нажатии периода выдает словарь с выбранными параметрами
@router.callback_query(F.data.in_([LEXICON['but_5'], LEXICON['but_6'], LEXICON['but_7'], LEXICON['but_8']]))
async def period(callback: CallbackQuery):
    user_data['period'] = callback.data
    await callback.message.answer(
        text=f'Вы выбрали{user_data}'
    )
    await callback.answer()