from aiogram import Router, F

from aiogram.filters import Command, CommandStart, StateFilter

from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON_ENG

from models.queries import * 

from keyboards.weekdays_kb import weekdays_keyboard

from keyboards.manage_plan_kb import manage_keyboard

from services.show_plan import show_plan

from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import State, StatesGroup, default_state

from aiogram.fsm.storage.memory import MemoryStorage


# init storage for our states
storage: MemoryStorage = MemoryStorage()



# class for FSM context
class UserPlanFSM(StatesGroup):
    # user's answer
    user_plan = State()



# init Router
router: Router = Router()

# Handler for /start command
@router.message(CommandStart(), StateFilter(default_state))
async def start_command(message: Message):
    await message.answer(
        text=LEXICON_ENG.get(message.text, LEXICON_ENG["others"])
    )

    # adding the new data into our db. We add the user's telegram id.
    add_data(id_user=message.from_user.id)


# Handler for /help command
@router.message(Command(commands="help"), StateFilter(default_state))
async def help_command(message: Message):
    await message.answer(
        text=LEXICON_ENG.get(message.text, LEXICON_ENG["others"])
    )


# Handler for /show command
@router.message(Command(commands="show"), StateFilter(default_state))
async def show_command(message: Message):

    await message.answer(
        text=LEXICON_ENG.get(message.text, LEXICON_ENG["others"]),
        reply_markup=weekdays_keyboard()
    )


# Callback handler for weekdays
@router.callback_query(F.data.in_(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]), StateFilter(default_state))
async def callback_weekdays(callback: CallbackQuery,  state: FSMContext):

    if not get_user(callback.from_user.id):
        add_data(callback.from_user.id)
    #-----------------------------------------
    await state.update_data(day=callback.data)
    #-----------------------------------------
    print(f"User id in 'callback_weekdays' function is {callback.from_user.id}")
    await callback.message.edit_text(
        text= show_plan(callback.from_user.id, callback.data),
        reply_markup=manage_keyboard()
    )
    


# Callback handler for back command
@router.callback_query(F.data == "back", StateFilter(default_state))
async def callback_back_command(callback: CallbackQuery, state: FSMContext):

    print(f"This is function 'callback_back_command' wiht this day - {callback.message.text.split()[5]}")
    await callback.message.edit_text(
        text=LEXICON_ENG["/show"],
        reply_markup=weekdays_keyboard()
    )


# Callback handler for change command
@router.callback_query(F.data == "change", StateFilter(default_state))
async def callback_change_command(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_text(
        text=LEXICON_ENG["write"],
        reply_markup=manage_keyboard()
    )

    await state.set_state(UserPlanFSM.user_plan)


# Callback handler for clear command
@router.callback_query(F.data == "clear", StateFilter(default_state))
async def callback_clear_command(callback: CallbackQuery, state: FSMContext):
    # we get text with our buttons. Then we use str.split() method to cut text
    # Then we get our day buy index (it will have 5th index). Then we must cut symbol ':' from the end of the word 
    day = callback.message.text.split()[5][:-1]                                         

    update_data(callback.from_user.id, day, "Empty")

    await callback.message.edit_text(
        text= show_plan(callback.from_user.id, day),
        reply_markup=manage_keyboard()
    )


# Callback handler for finishing and resulting FSM Context
@router.message(StateFilter(UserPlanFSM.user_plan))
async def process_plan(message: Message, state: FSMContext):

    await state.update_data(plan=message.text)

    user_plan = await state.get_data()

    if user_plan:
        
        id_user = message.from_user.id
        day = user_plan["day"]
        plan = user_plan["plan"]

        print(f"This is fucntion 'process_plan'. User's is is {message.from_user.id} ")
        update_data(id_user, day, plan)

    await message.answer(
        text= show_plan(id_user, day),
        reply_markup= manage_keyboard()
    )

    await state.clear()



