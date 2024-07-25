from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON

from classes.Onecallbackfactory import StatusCallbackFactory

def creat_inlinekb (width: int,
                    *args: str,
                    cbd: str = None,
                    last_btn: str = None,
                    **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button if cbd == None else StatusCallbackFactory(status=cbd, name=button).pack()))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button if cbd == None else StatusCallbackFactory(status=cbd, name=button).pack()))
    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'
        ))

    return kb_builder.as_markup()