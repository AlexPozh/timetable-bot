from aiogram import Router

from aiogram.types import Message

from lexicon.lexicon import LEXICON_ENG
# init Router
router: Router = Router()


@router.message()
async def echo(message: Message):
    await message.reply(
        text=LEXICON_ENG["others"]
    )