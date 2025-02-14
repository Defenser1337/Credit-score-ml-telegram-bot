from aiogram import F, Router
from aiogram.types import  Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from pathlib import Path

import keyboards as kb

import joblib
import pandas as pd


MODEL_PATH = Path.cwd() / 'code' / 'models' / 'model.pkl'

if not MODEL_PATH.exists():
    raise ValueError(f"Model is not found in {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

router = Router()

class Survey(StatesGroup):
    Age = State()
    Occupation = State()
    Annual_Income = State()
    Monthly_Inhand_Salary = State()
    Num_Bank_Accounts = State()
    Num_Credit_Card = State()
    Interest_Rate = State()
    Num_of_Loan = State()
    Delay_from_due_date = State()
    Num_of_Delayed_Payment = State()
    Changed_Credit_Limit = State()
    Num_Credit_Inquiries = State()
    Credit_Mix = State()
    Outstanding_Debt = State()
    Credit_Utilization_Ratio = State()
    Credit_History_Age = State()
    Payment_of_Min_Amount = State()
    Total_EMI_per_month = State()
    Amount_invested_monthly = State()
    Payment_Behaviour = State()
    Monthly_Balance = State()

def model_predict(X : pd.DataFrame, model) -> str:
    y_pred = model.predict(X)

    if y_pred[0] == True:
        return "Congratulations! 🎉 🎉 🎉 You have a good credit score!"
    else:
        return "Unfortunately. You have a bad credit rating. Try to build up your credit history. Increase your income or change the way you approach your loans."


@router.message(Command('start'))
async def cmd_start(message : Message):
    await message.answer(
        text = 'Hi, this is a bot that determines your credit score, in order to get your credit score, you will need to fill in your details and then the machine learning model will make a prediction.',
        reply_markup=kb.lets_go_markup)

@router.callback_query(F.data == 'lets_go')
async def start_survey(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Survey.Age)
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer("[1/21] Enter your age:")

@router.message(StateFilter(Survey.Age))
async def survey_age(message: Message, state: FSMContext):
    try:
        user_age = int(message.text)
        if user_age < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Age = user_age)
        await state.set_state(Survey.Occupation)
        await message.answer(text = "[2/21] Choose your occupation",
                             reply_markup = kb.occupation_markup)
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.callback_query(StateFilter(Survey.Occupation))
async def survey_occupation(callback: CallbackQuery, state: FSMContext):
    user_data = callback.data
    await state.update_data(Occupation = user_data)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.set_state(Survey.Annual_Income)
    await callback.message.answer("[3/21] Enter your annual income in USD:")

@router.message(StateFilter(Survey.Annual_Income))
async def survey_annual_income(message: Message, state: FSMContext):
    try:
        user_value = float(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Annual_Income = user_value)
        await state.set_state(Survey.Monthly_Inhand_Salary)
        await message.answer(text = "[4/21] Enter the monthly base salary in USD:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Monthly_Inhand_Salary))
async def survey_monthly_inhand_salary(message: Message, state: FSMContext):
    try:
        user_value = float(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Monthly_Inhand_Salary = user_value)
        await state.set_state(Survey.Num_Bank_Accounts)
        await message.answer(text = "[5/21] Enter the number of your bank accounts:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Num_Bank_Accounts))
async def survey_num_bank_accounts(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Num_Bank_Accounts = user_value)
        await state.set_state(Survey.Num_Credit_Card)
        await message.answer(text = "[6/21] Enter the number of your credit cards:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Num_Credit_Card))
async def survey_num_credit_card(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Num_Credit_Card = user_value)
        await state.set_state(Survey.Interest_Rate)
        await message.answer(text = "[7/21] Enter the Interest Rate (Credit Rate) on your credit card in %. If you do not have one, enter 0:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Interest_Rate))
async def survey_interest_rate(message: Message, state: FSMContext):
    try:
        user_value = float(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Interest_Rate = user_value)
        await state.set_state(Survey.Num_of_Loan)
        await message.answer(text = "[8/21] Enter the number of your loans in the bank:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Num_of_Loan))
async def survey_num_of_loan(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Num_of_Loan = user_value)
        await state.set_state(Survey.Delay_from_due_date)
        await message.answer(text = "[9/21] Enter the average number of days late on the loan. If you have had no loans, enter 0:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Delay_from_due_date))
async def survey_delay_from_due_date (message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Delay_from_due_date = user_value)
        await state.set_state(Survey.Num_of_Delayed_Payment)
        await message.answer(text = "[10/21] Enter the average number of your credit delays:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Num_of_Delayed_Payment))
async def survey_num_of_delayed_payment (message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Num_of_Delayed_Payment = user_value)
        await state.set_state(Survey.Changed_Credit_Limit)
        await message.answer(text = "[11/21] By how much percent your last interest rate (credit rate) changed:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Changed_Credit_Limit))
async def survey_changed_credit_limit(message: Message, state: FSMContext):
    try:
        user_value = float(message.text)
        await state.update_data(Changed_Credit_Limit = user_value)
        await state.set_state(Survey.Num_Credit_Inquiries)
        await message.answer(text = "[12/21] Enter how many times you have received a credit card:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Num_Credit_Inquiries))
async def survey_num_credit_inquiries(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Num_Credit_Inquiries = user_value)
        await state.set_state(Survey.Credit_Mix)
        await message.answer(text = "[13/21] Choose how well you combine multiple credits",
                             reply_markup=kb.credit_mix_markup)
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.callback_query(StateFilter(Survey.Credit_Mix))
async def survey_credit_mix(callback: CallbackQuery, state: FSMContext):
    user_data = callback.data
    await state.update_data(Credit_Mix = user_data)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.set_state(Survey.Outstanding_Debt)
    await callback.message.answer("[14/21] Enter your current debt in USD:")

@router.message(StateFilter(Survey.Outstanding_Debt))
async def survey_outstanding_debt(message: Message, state: FSMContext):
    try:
        user_value = float(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Outstanding_Debt = user_value)
        await state.set_state(Survey.Credit_Utilization_Ratio)
        await message.answer(text = "[15/21] Rate how often you use your credit card, as a percentage from 0 to 100:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Credit_Utilization_Ratio))
async def survey_credit_utilization_ratio(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0 or user_value > 100:
            raise ValueError("Value is incorrect.")
        await state.update_data(Credit_Utilization_Ratio = user_value)
        await state.set_state(Survey.Credit_History_Age)
        await message.answer(text = "[16/21] How many years your credit history has existed in years:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.message(StateFilter(Survey.Credit_History_Age))
async def survey_credit_history_age(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Credit_History_Age = user_value)
        await state.set_state(Survey.Payment_of_Min_Amount)
        await message.answer(text = "[17/21] You are more likely to pay only the minimum payment:",
                             reply_markup=kb.min_payment_markup)
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.callback_query(StateFilter(Survey.Payment_of_Min_Amount))
async def survey_payment_of_min_amount(callback: CallbackQuery, state: FSMContext):
    user_data = callback.data
    await state.update_data(Payment_of_Min_Amount = user_data)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.set_state(Survey.Total_EMI_per_month)
    await callback.message.answer("[18/21] Enter your latest EMI on the loan in USD:")

@router.message(StateFilter(Survey.Total_EMI_per_month))
async def survey_total_emi_per_month(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Total_EMI_per_month = user_value)
        await state.set_state(Survey.Amount_invested_monthly)
        await message.answer(text = "[19/21] Enter the amount you are investing per month in USD:")
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")


@router.message(StateFilter(Survey.Amount_invested_monthly))
async def survey_amount_invested_monthly(message: Message, state: FSMContext):
    try:
        user_value = float(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Amount_invested_monthly = user_value)
        await state.set_state(Survey.Payment_Behaviour)
        await message.answer(text = "[20/21] How do you usually behave with your expenses",
                             reply_markup=kb.payment_behaviour_markup)
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")

@router.callback_query(StateFilter(Survey.Payment_Behaviour))
async def survey_payment_behaviour(callback: CallbackQuery, state: FSMContext):
    user_data = callback.data
    await state.update_data(Payment_Behaviour = user_data)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.set_state(Survey.Monthly_Balance)
    await callback.message.answer("[21/21] How much on average is stored in your balance per month in USD:")

@router.message(StateFilter(Survey.Monthly_Balance))
async def survey_monthly_balance(message: Message, state: FSMContext):
    try:
        user_value = int(message.text)
        if user_value < 0:
            raise ValueError("Value must be non-negative.")
        await state.update_data(Monthly_Balance = user_value)

        survey_dict = await state.get_data()

        survey_df = pd.DataFrame([survey_dict])

        model_prediction = model_predict(survey_df, model)

        await message.answer(model_prediction)
        await message.answer("To check your credit rating again: write the command /start")
        await state.clear()
        return
    except ValueError:
        await message.answer("Error: The value is incorrect. Enter value again:")





