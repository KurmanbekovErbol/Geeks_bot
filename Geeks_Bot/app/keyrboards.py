from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


buttons = [
    [KeyboardButton(text='О вас'), KeyboardButton(text='О направлениях'), KeyboardButton(text='О контактах')],
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')

Direction = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Назад')],
    [KeyboardButton(text='backend'), KeyboardButton(text='frontend')],
    [KeyboardButton(text='uxui'), KeyboardButton(text='fullstack')],
], resize_keyboard=True,  input_field_placeholder='Выберите кнопку')