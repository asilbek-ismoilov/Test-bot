from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

option = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="A"), 
            InlineKeyboardButton(text="B", callback_data="B"), 
            InlineKeyboardButton(text="C", callback_data="C"), 
            InlineKeyboardButton(text="D", callback_data="D"), 
        ]
    ]
)

ask = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="true"), 
            InlineKeyboardButton(text="❌", callback_data="false"), 
        ]
    ]
)

