from loader import dp, qb, bot
from aiogram.types import Message, Poll, PollAnswer, CallbackQuery
from aiogram import F
from keyboard_buttons.inline.menu import start_test
from aiogram.fsm.context import FSMContext
import asyncio

user_answers = {}
user_polls = {}

@dp.message(lambda message: message.text in list(set(row[0] for row in qb.question_names())))
async def test_start(message: Message, state: FSMContext):
    test_name = message.text
    await state.update_data(test_name=test_name)
    question_number = len(qb.get_questions(test_name))
    text = f"Test nomi: <b>{test_name}</b> [<b>{question_number}</b>] \nTestni boshlash uchun <b>\"Boshlash\"</b> degan tugmani bosing !"
    await message.answer(text, parse_mode="html", reply_markup=start_test)

@dp.callback_query(F.data == "start")
async def start(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    test_name = data.get("test_name")
    questions = qb.get_questions(test_name)
    
    if not questions:
        await call.message.answer("Bu test bo'yicha savollar topilmadi!")
        return
    
    user_id = call.from_user.id
    user_answers[user_id] = {"correct": 0, "wrong": 0, "total": len(questions)}
    
    for question in questions:
        test_name, q_text, a, b, c, d, answer = question
        options = [a, b, c, d]

        if answer in ["A", "B", "C", "D"]:
            correct_option_id = ["A", "B", "C", "D"].index(answer)
        else:
            correct_option_id = options.index(answer)

        poll_message = await bot.send_poll(
            chat_id=call.message.chat.id,
            question=q_text,
            options=options,
            type="quiz",
            correct_option_id=correct_option_id,
            is_anonymous=False
        )
        
        if user_id not in user_polls:
            user_polls[user_id] = {}
        user_polls[user_id][poll_message.poll.id] = correct_option_id
        
        try:
            await asyncio.sleep(10)
            if poll_message.poll.id in user_polls[user_id]:
                user_answers[user_id]["wrong"] += 1  
        except Exception as e:
            print("Error:", e)

    correct = user_answers[user_id]["correct"]
    wrong = user_answers[user_id]["wrong"]
    total = user_answers[user_id]["total"]
    full_name = call.from_user.full_name
    
    await call.message.answer(f"{full_name} siz {test_name} savollar toplamidan {correct} tasini to'g'ri va {wrong} tasini xato yechdingiz 🎉")
    del user_answers[user_id]
    del user_polls[user_id]

@dp.poll_answer()
async def handle_poll_answer(poll_answer: PollAnswer):
    user_id = poll_answer.user.id
    poll_id = poll_answer.poll_id
    user_choice = poll_answer.option_ids[0]
    
    if user_id in user_polls and poll_id in user_polls[user_id]:
        correct_answer = user_polls[user_id].pop(poll_id)
        
        if user_choice == correct_answer:
            user_answers[user_id]["correct"] += 1
        else:
            user_answers[user_id]["wrong"] += 1
