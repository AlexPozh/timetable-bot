from aiogram import F, Bot, Dispatcher

from config_data.config import Config_bot

import asyncio

from keyboards.main_menu import set_main_menu

from handlers import user_handlers, others_handlers

from models.queries import * 


async def main() -> None:
    
    bot: Bot = Bot(token=Config_bot.bot_token,
                   parse_mode="HTML")

    dp: Dispatcher = Dispatcher()

    # calls the main menu function
    await set_main_menu(bot)

    # calls the connection function with our database


    # include routers from handlers module
    dp.include_router(user_handlers.router)
    dp.include_router(others_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    asyncio.run(main())



