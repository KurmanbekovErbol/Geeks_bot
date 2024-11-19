from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message
from app.keyrboards import *

router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer('Здравствуйте, спасибо, что обратились к нам! Что вы хотите узнать о Geeks?', reply_markup=keyboard)

@router.message(F.text == 'Назад')
async def back(message: Message):
    await message.answer('Что вы хотите узнать от Geeks?', reply_markup=keyboard)

@router.message(F.text == 'О вас')
async def About_Us(message: Message):
    await message.answer("""Международная IT-академия Geeks (Гикс) был основан Fullstack-
разработчиком Айдаром Бакировым и Android-разработчиком 
Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать 
возможность каждому человеку, даже без опыта в технологиях, 
гарантированно освоить IT-профессию.""")

@router.message(F.text == 'О направлениях')
async def Directions(message: Message):
    await message.answer('Выберите направление', reply_markup=Direction)

@router.message(F.text == 'О контактах')
async def Contacts(message: Message):
    await message.reply_contact(phone_number='+996557052018', last_name='Geeks', first_name='Администрация')

@router.message(F.text == 'backend')
async def backend(message: Message):
    await message.answer("""Backend - занимается разработкой серверной части веб-приложений и сайтов. Он отвечает за работу баз данных, серверов и логику, которая происходит на серверной стороне. 
Стоимость: 12000 сом в месяц. 
Обучение: 5 месяц""")

@router.message(F.text == 'frontend')
async def frontend(message: Message):
    await message.answer("""Frontend - занимается созданием клиентской части веб-приложений, сайтов, которая взаимодействует с пользователем
Стоимость: 16000 сом в месяц. 
Обучение: 5 месяц""")

@router.message(F.text == 'uxui')
async def uxui(message: Message):
    await message.answer("""UI ― это user interface, пользовательский интерфейс, проще говоря ― оформление сайта: сочетания цветов, шрифты, иконки и кнопки. UX ― это функционал интерфейса, UI ― его внешний вид.
Стоимость: 16000 сом в месяц. 
Обучение: 4 месяц""")

@router.message(F.text == 'fullstack')
async def fullstack(message: Message):
    await message.answer("""Fullstack-разработчик занимается веб-разработкой полного цикла. Обычно он создает веб-приложения, в которых делает сразу все: проектирует архитектуру, разрабатывает frontend- и backend-части, привязывает проект к базе данных, обновляет его и занимается системным администрированием
Стоимость: 16000 сом в месяц. 
Обучение: 10 месяц""")