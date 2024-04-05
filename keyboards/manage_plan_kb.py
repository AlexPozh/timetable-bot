from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon import LEXICON_ENG



def manage_keyboard() -> InlineKeyboardMarkup:
    """Function creates inline buttons to manage the plan."""

    # init the inline builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(
        *[
            InlineKeyboardButton(
                text=LEXICON_ENG["back"],
                callback_data="back"
            ),
            InlineKeyboardButton(
                text=LEXICON_ENG["change"],
                callback_data="change"
            ),
            InlineKeyboardButton(
                text=LEXICON_ENG["clear_all"],
                callback_data="clear"
            ),
        ]
    )

    return kb_builder.as_markup()