from aiogram import Router, F
from aiogram.filters import CommandStart
from keyboards.creat_inlinekb import creat_inlinekb
from aiogram.types import Message, CallbackQuery


router= Router()

user_data={}

@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = creat_inlinekb(1, 'платежи', 'заказы')
    await message.answer(
        text='Выберите что будем настраивать',
        reply_markup=keyboard
    )

@router.callback_query(F.data == "платежи")
async def send_random_value(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, 'просроченные', 'сегодня', 'на этой неделе', 'в этом месяце', 'очистить выбор', 'отменить последний выбор', last_btn='подтвердить')
    await callback.message.edit_text(
        text='Какой период',
        reply_markup=keyboard
    )
    await callback.answer()

@router.callback_query(F.data == "заказы")
async def send_random_value(callback: CallbackQuery):
    keyboard = creat_inlinekb(1, 'просроченные', 'сегодня', 'на этой неделе', 'в этом месяце', 'очистить выбор', 'отменить последний выбор', last_btn='подтвердить')
    await callback.message.edit_text(
        text='Какой период',
        reply_markup=keyboard
    )

assembly = set()
word = []

@router.callback_query(F.data.in_({'просроченные', 'сегодня', 'на этой неделе', 'в этом месяце'}))
async def press_and_assembly(callback: CallbackQuery):
    assembly.add(callback.data)
    word.append(callback.data)
    await callback.answer(
        text=f'вы выбрали "{callback.data}"')

@router.callback_query(F.data == 'отменить последний выбор')
async def cancel_assembly(callback: CallbackQuery):
    assembly.discard(word[-1])
    await callback.answer(
        text=f'вы убрали "{word[-1]}"')

@router.callback_query(F.data == 'очистить выбор')
async def clear(callback: CallbackQuery):
    assembly.clear()
    await callback.answer(
        text='Вы очистили список',
        show_alert=True
    )

@router.callback_query(F.data == 'last_btn')
async def press_and_assembly(callback: CallbackQuery):
    await callback.answer(
        text=f'вы выбрали {assembly}',
        show_alert=True
    )
    await callback.answer()
