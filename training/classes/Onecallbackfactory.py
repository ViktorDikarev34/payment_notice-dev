from aiogram.filters.callback_data import CallbackData



class StatusCallbackFactory(CallbackData, prefix='status'):
    status: str
    name: str
