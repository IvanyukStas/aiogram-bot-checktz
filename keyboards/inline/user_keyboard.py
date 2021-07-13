from aiogram import types

acept_buttons = [types.InlineKeyboardButton('Беру в работу!', callback_data='acept'),
                 types.InlineKeyboardButton('Отказаться', callback_data='cancel')]
acept_keyboard = types.InlineKeyboardMarkup(row_width=2)
acept_keyboard.add(*acept_buttons)
