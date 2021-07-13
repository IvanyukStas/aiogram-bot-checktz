from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.db_api.sqlite_db import get_task

categories = ['Shar', 'Idsk', 'add_user_to_bd', 'usb', 'Clock', 'INVENTORY']
buttons = []
for category in categories:
    if not get_task(category) == []:
        button = InlineKeyboardButton(category, callback_data='btn_'+category)
        buttons.append(button)
categories_kb = InlineKeyboardMarkup(row_width=3)
categories_kb.add(*buttons)
