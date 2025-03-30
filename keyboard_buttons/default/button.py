from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from loader import qb


def get_buttun():
    questions = list(set(row[0] for row in qb.question_names()))

    question_button = ReplyKeyboardBuilder()

    for question in questions:
        question_button.add(KeyboardButton(text=question))

    question_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

    question_button.adjust(2)

    return question_button.as_markup(resize_keyboard=True, input_field_placeholder="Tugmalardan birini tanlang...")