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
        text=LEXICON['/start'],
        reply_markup=keyboard
    )

spisok_tipo_ms = ['новый', 'не оплачено', 'оплачено']
assembly = set()

#При нажатии платежи выдает следующее сообщение "какой статус" и кнопки из списка, можно выбирать несколько
@router.callback_query(F.data == LEXICON['but_1'])
async def send_random_value_payment(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, spisok_tipo_ms[0], spisok_tipo_ms[1], spisok_tipo_ms[2], last_btn=LEXICON['but_4'])
    user_data['{callback.data}'] = {}
    await callback.message.edit_text( # type: ignore
        text=LEXICON['but_3'],
        reply_markup=keyboard
    )
    await callback.answer()

#При нажатии заказы выдает следующее сообщение "какой статус" и кнопки из списка, можно выбирать несколько
@router.callback_query(F.data == LEXICON['but_2'])
async def send_random_value(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, spisok_tipo_ms[0], spisok_tipo_ms[1], spisok_tipo_ms[2], last_btn=LEXICON['but_4'])
    user_data['{callback.data}'] = {}
    await callback.message.edit_text(  # type: ignore
        text=LEXICON['but_3'],
        reply_markup=keyboard
    )
    await callback.answer()

#

#При нажатии кнопки подтвердить выдает сообщение с кнопками периода
@router.callback_query(F.data == 'last_btn')
async def press_and_assembly(callback: CallbackQuery):
    keyboard = creat_inlinekb(2, LEXICON['but_5'], LEXICON['but_6'], LEXICON['but_7'], LEXICON['but_8'] )
    await callback.message.edit_text( # type: ignore
        text = LEXICON['but_9'],
        reply_markup = keyboard
    )
    await callback.answer('Вы выбрали')
