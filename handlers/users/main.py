from loader import dp, bot
from aiogram.types import Message
from aiogram import F

# Poll (so'rovnoma) yuborish
# await bot.send_poll(
#     chat_id=callback.message.chat.id,  # Callback kelgan chat ID
#     question=question,  # Savol
#     options=[a, b, c, d],  # Variantlar
#     is_anonymous=False,  # Ovoz berish ochiq bo'lsin
#     type="quiz",  # Test rejimi
#     correct_option_id=["A", "B", "C", "D"].index(answer) if answer in ["A", "B", "C", "D"] else 0  # To'g'ri javobni aniqlash
# )
