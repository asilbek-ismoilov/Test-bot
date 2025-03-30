from loader import dp,qb, ADMINS
from aiogram.types import Message, CallbackQuery
from filters.admin import IsBotAdminFilter
from aiogram import F
from states.add_questions import Questions
from aiogram.fsm.context import FSMContext
from keyboard_buttons.inline.menu import option
from aiogram.types import ReplyKeyboardRemove
from keyboard_buttons.inline.menu import ask
import asyncio
from keyboard_buttons.default.button import get_buttun

@dp.message(F.text=="Savol qo'shish",IsBotAdminFilter(ADMINS))
async def add_questions(message:Message, state:FSMContext):
    await message.answer("<b>🗂 Yangi savollar to'plamini yaratish uchun nom kiriting</b>", parse_mode="html",reply_markup=ReplyKeyboardRemove())

    await state.set_state(Questions.test_name)

@dp.message(F.text, Questions.test_name)
async def test_name(message:Message, state:FSMContext):
    test_name = message.text
    await state.update_data(test_name=test_name)
    await message.answer(text="Savolni yozing !")

    await state.set_state(Questions.question)

@dp.message(Questions.test_name)
async def test_name_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.message(F.text, Questions.question)
async def question(message:Message, state:FSMContext):
    question = message.text
    await state.update_data(question=question)
    await message.answer(text="A variant javobini yozing !")

    await state.set_state(Questions.a)

@dp.message(Questions.question)
async def question_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.message(F.text, Questions.a)    
async def a(message:Message, state:FSMContext):
    a = message.text.upper()
    await state.update_data(a=a)
    await message.answer(text="B variant javobini yozing !")

    await state.set_state(Questions.b)

@dp.message(Questions.a)
async def a_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.message(F.text, Questions.b)
async def b(message:Message, state:FSMContext):
    b = message.text.upper()
    await state.update_data(b=b)
    await message.answer(text="C variant javobini yozing !")

    await state.set_state(Questions.c)

@dp.message(Questions.b)
async def b_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.message(F.text, Questions.c)
async def c(message:Message, state:FSMContext):
    c = message.text.upper()
    await state.update_data(c=c)
    await message.answer(text="D variant javobini yozing !")

    await state.set_state(Questions.d)

@dp.message(Questions.c)
async def c_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.message(F.text, Questions.d)
async def d(message: Message, state: FSMContext):    
    d = message.text.upper()
    await state.update_data(d=d)
    await message.answer(text="Javobni tanlang !", reply_markup=option)

    await state.set_state(Questions.answer)

@dp.message(Questions.d)
async def d_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.callback_query(F.data, Questions.answer)
async def answer(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    data = await state.get_data()
    test_name = data.get("test_name")
    question = data.get("question")
    a = data.get("a")
    b = data.get("b")
    c = data.get("c")
    d = data.get("d")
    answer = callback.data

    qb.add_questions(
        test_name=test_name, 
        question=question, 
        a=a, b=b, c=c, d=d, 
        answer=answer
    )

    message_del = await callback.message.answer("Savol qo'shildi 🎉")
    
    await state.clear()
    await callback.message.answer("Savolni qo'shishni davom etasizmi ?", reply_markup=ask)

    await asyncio.sleep(3)
    await message_del.delete()

@dp.message(Questions.answer)
async def answer_del(message:Message, state:FSMContext):
    await message.answer(text= "Faqat matn yozing, boshqa fayllar mumkin emas ! ")
    await message.delete()

@dp.callback_query(F.data == "true")
async def add_another_question(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("<b>🗂 Yangi savollar to'plamini yaratish uchun nom kiriting \nyoki Tugmalardan birini tanling</b>", parse_mode="html", reply_markup=get_buttun())
    await state.set_state(Questions.test_name)

@dp.callback_query(F.data == "false")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()

    await callback.message.answer("Menu", reply_markup=get_buttun())
    await state.clear()