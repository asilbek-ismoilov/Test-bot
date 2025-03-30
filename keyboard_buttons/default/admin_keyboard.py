from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
            KeyboardButton(text="Savol qo'shish"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

# def menu(language):
#     main_menu = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(),
#             ]
            
#         ],
#        resize_keyboard=True,
#        input_field_placeholder="Menudan birini tanlang"
#     )
#     return menu