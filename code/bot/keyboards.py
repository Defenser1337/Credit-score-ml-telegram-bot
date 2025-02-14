from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

lets_go_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Let's go!",
                                                                             callback_data="lets_go")]])

occupation_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Scientist",
                                                                             callback_data="Scientist")],
                                                          [InlineKeyboardButton(text="Teacher",
                                                                                callback_data="Teacher")],
                                                          [InlineKeyboardButton(text="Engineer",
                                                                                callback_data="Engineer")],
                                                          [InlineKeyboardButton(text="Entrepreneur",
                                                                                callback_data="Entrepreneur")],
                                                          [InlineKeyboardButton(text="Developer",
                                                                                callback_data="Developer")],
                                                          [InlineKeyboardButton(text="Lawyer",
                                                                                callback_data="Lawyer")],
                                                          [InlineKeyboardButton(text="Media Manager",
                                                                                callback_data="Media_Manager")],
                                                          [InlineKeyboardButton(text="Doctor",
                                                                                callback_data="Doctor")],
                                                          [InlineKeyboardButton(text="Journalist",
                                                                                callback_data="Journalist")],
                                                          [InlineKeyboardButton(text="Manager",
                                                                                callback_data="Manager")],
                                                          [InlineKeyboardButton(text="Accountant",
                                                                                callback_data="Accountant")],
                                                          [InlineKeyboardButton(text="Musician",
                                                                                callback_data="Musician")],
                                                          [InlineKeyboardButton(text="Mechanic",
                                                                                callback_data="Mechanic")],
                                                          [InlineKeyboardButton(text="Writer",
                                                                                callback_data="Writer")],
                                                          [InlineKeyboardButton(text="Architect",
                                                                                callback_data="Architect")],
                                                          [InlineKeyboardButton(text="None of the above",
                                                                                callback_data="_______")]
                                                          ])

credit_mix_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Good",
                                                                             callback_data="Good")],
                                                          [InlineKeyboardButton(text="Standard",
                                                                                callback_data="Standard")],
                                                          [InlineKeyboardButton(text="Bad",
                                                                                callback_data="Bad")],
                                                          [InlineKeyboardButton(text="Didn't have multiple loans",
                                                                                callback_data="_")]
                                                          ])

min_payment_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Yes",
                                                                             callback_data="Yes")],
                                                          [InlineKeyboardButton(text="No",
                                                                                callback_data="No")],
                                                          [InlineKeyboardButton(text="Not sure",
                                                                                callback_data="NM")]
                                                          ])


payment_behaviour_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "I spend a lot in small amounts",
                                                                                        callback_data="High_spent_Small_value_payments")],
                                                                 [InlineKeyboardButton(text="I spend a lot in normal amounts",
                                                                                        callback_data="High_spent_Medium_value_payments")],
                                                                 [InlineKeyboardButton(text="I spend a lot in large amounts",
                                                                                        callback_data="High_spent_Large_value_payments")],
                                                                 [InlineKeyboardButton(text="I spend a little in small amounts",
                                                                                        callback_data="Low_spent_Small_value_payments")],
                                                                 [InlineKeyboardButton(text="I spend a little in normal amounts",
                                                                                        callback_data="Low_spent_Medium_value_payments")],
                                                                 [InlineKeyboardButton(text="I spend a little in large amounts",
                                                                                        callback_data="Low_spent_Large_value_payments")],
                                                                 [InlineKeyboardButton(text="None of the above are suitable",
                                                                                        callback_data="!@9#%8")]
                                                                 ])
