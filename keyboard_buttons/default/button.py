from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from loader import qb


questions = [row[0] for row in qb.question_names()]

question_button = ReplyKeyboardBuilder()

for question in questions:
    question_button.add(KeyboardButton(text=question))

question_button.add(KeyboardButton(text="Orqaga qaytish 🔙"))

question_button.adjust(3)

question_button = question_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Kompyuterni tanlang..."
)