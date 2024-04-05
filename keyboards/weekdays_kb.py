from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_DAYS


def weekdays_keyboard() -> InlineKeyboardMarkup:
    """Function creates the inline keyboard with the weekdays"""

    # init inline keyboard builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(
        *[
            InlineKeyboardButton(
            text=short_title,
            callback_data=long_title) for long_title, short_title in LEXICON_DAYS.items()
            ]
    )

    return kb_builder.as_markup()

