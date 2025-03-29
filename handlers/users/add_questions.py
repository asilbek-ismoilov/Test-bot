from loader import dp,ADMINS
from aiogram.types import Message
from filters.admin import IsBotAdminFilter
from aiogram import F
from states.add_questions import Questions
from aiogram.fsm.context import FSMContext
from keyboard_buttons.inline.menu import option

@dp.message(F.text=="Savol qo'shish",IsBotAdminFilter(ADMINS))
async def add_questions(message:Message, state:FSMContext):
    await message.answer(text="Savol nomini yozing !")

    await state.set_state(Questions.test_name)

@dp.message(Questions.test_name)
async def test_name(message:Message, state:FSMContext):
    test_name = message.text
    await state.update_data(test_name=test_name)
    await message.answer(text="Savolni yozing !")

    await state.set_state(Questions.question)


@dp.message(Questions.question)
async def question(message:Message, state:FSMContext):
    question = message.text
    await state.update_data(question=question)
    await message.answer(text="A variantini yozing !")

    await state.set_state(Questions.a)


@dp.message(Questions.a)    
async def a(message:Message, state:FSMContext):
    a = message.text
    await state.update_data(a=a)
    await message.answer(text="B variantini yozing !")

    await state.set_state(Questions.b)

@dp.message(Questions.b)
async def b(message:Message, state:FSMContext):
    b = message.text
    await state.update_data(b=b)
    await message.answer(text="C variantini yozing !")

    await state.set_state(Questions.c)

@dp.message(Questions.c)
async def c(message:Message, state:FSMContext):
    c = message.text
    await state.update_data(c=c)
    await message.answer(text="D variantini yozing !")

    await state.set_state(Questions.d)

@dp.message(Questions.d)
async def d(message:Message, state:FSMContext):    
    d = message.text
    await state.update_data(d=d)
    await message.answer(text="Javobni yozing !")

    await state.set_state(Questions.answer, reply_markup=option)

@dp.c(Questions.answer)
async def answer(message:Message, state:FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    data = await state.get_data()
    test_name = data.get("test_name")
    question = data.get("question")
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    d = data.get("d")
    answer = data.get("answer")


