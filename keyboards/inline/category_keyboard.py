from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categories = ['Shar', 'Idsk', 'add_user_to_bd', 'usb', 'Clock', 'INVENTORY']
buttons = []
for category in categories:
    button = InlineKeyboardButton(category, callback_data='btn_'+category)
    buttons.append(button)
categories_kb = InlineKeyboardMarkup(row_width=1)
categories_kb.add(*buttons)
