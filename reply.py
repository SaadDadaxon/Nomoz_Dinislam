from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕰Nomoz Vaqtlari"),
            KeyboardButton(text="📌Manzil", request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
