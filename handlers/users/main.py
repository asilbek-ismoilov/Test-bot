from loader import dp, qb, bot
from aiogram.types import Message, Poll, PollAnswer
from aiogram import F

@dp.message(lambda message: message.text in list(set(row[0] for row in qb.question_names())))
async def start_test(message: Message):
    test_name = message.text
    questions = qb.get_questions(test_name)
    
    if not questions:
        await message.answer("Bu test bo'yicha savollar topilmadi!")
        return
    
    user_answers[message.from_user.id] = {"correct": 0, "total": len(questions)}
    
    for question in questions:
        test_name, q_text, a, b, c, d, answer = question
        options = [a, b, c, d]

        if answer in ["A", "B", "C", "D"]:
            correct_option_id = ["A", "B", "C", "D"].index(answer)
        else:
            correct_option_id = options.index(answer)

        
        poll_message = await bot.send_poll(
            chat_id=message.chat.id,
            question=q_text,
            options=options,
            type="quiz",
            correct_option_id=correct_option_id,
            is_anonymous=False
        )
        
        if message.from_user.id not in user_polls:
            user_polls[message.from_user.id] = {}

        user_polls[message.from_user.id][poll_message.poll.id] = correct_option_id


# Foydalanuvchi javob berganda natijani hisoblash
@dp.poll_answer()
async def handle_poll_answer(poll_answer: PollAnswer):
    user_id = poll_answer.user.id
    poll_id = poll_answer.poll_id
    user_choice = poll_answer.option_ids[0]
    
    if user_id in user_polls and poll_id in user_polls[user_id]:
        correct_answer = user_polls[user_id][poll_id]
        
        if user_choice == correct_answer:
            user_answers[user_id]["correct"] += 1

# Test natijalarini yuborish
@dp.message(F.text=="Natijam")
async def send_results(message: Message):
    user_id = message.from_user.id
    
    if user_id not in user_answers:
        await message.answer("Siz hali hech qanday test ishlamadingiz!")
        return
    
    correct = user_answers[user_id]["correct"]
    total = user_answers[user_id]["total"]
    
    await message.answer(f"Siz {total} ta savoldan {correct} tasini to'g'ri yechdingiz!")
    
    del user_answers[user_id]
    del user_polls[user_id]

# Foydalanuvchi javoblarini saqlash uchun dictionary
user_answers = {}
user_polls = {}


# await bot.send_poll(
#     chat_id=callback.message.chat.id,  # Callback kelgan chat ID
#     question=question,  # Savol
#     options=[a, b, c, d],  # Variantlar
#     is_anonymous=False,  # Ovoz berish ochiq bo'lsin
#     type="quiz",  # Test rejimi
#     correct_option_id=["A", "B", "C", "D"].index(answer) if answer in ["A", "B", "C", "D"] else 0  # To'g'ri javobni aniqlash
# )
