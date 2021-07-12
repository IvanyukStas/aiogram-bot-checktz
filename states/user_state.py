from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    registration = State()
    executor =State()