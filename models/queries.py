# from config_data.config import Config_database

import sqlite3

from lexicon.lexicon import LEXICON_DATABASE

import asyncio


def get_data_user(id_user: int, day: str) -> tuple[str]:
    """Getting data from db"""
    with sqlite3.connect("bot_users.db") as connect:
        cursor = connect.cursor()

        cursor.execute(
            f'SELECT {day} FROM plans WHERE id_users=?', (id_user,)
        )
        res = cursor.fetchone()
        print(f"This is 'get_data_user' function. It returned the following result - {res}. It got the following arguments: id_user - {id_user}.\nday - {day}")
        return res
    

def get_user(id_user: int = None) -> bool:
    """Boolean function which will return True if our db exists the user, otherwise False"""
    with sqlite3.connect("bot_users.db") as connect:
    
        cursor = connect.cursor()

        cursor.execute(
            f'SELECT id_users FROM plans WHERE id_users={id_user}'
        )
        res = cursor.fetchone()
        print(f"This is 'get_user' function. It returned id - {res}")
        return True if res else False


def update_data(id_user: int, day: str, schedule: str) -> None:
    """Updating data into the db"""
    with sqlite3.connect("bot_users.db") as connect:
    
        cursor = connect.cursor()

        cursor.execute(
            f'UPDATE plans SET {LEXICON_DATABASE[day]}=? WHERE id_users=?', (schedule, id_user)
        )
        
        connect.commit()
    

def add_data(id_user: int) -> None:
    """Adding new record into the db"""
    with sqlite3.connect("bot_users.db") as connect:
    
        cursor = connect.cursor()

        if not get_user(id_user):
            cursor.execute(
                'INSERT INTO plans VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (str(id_user), *["Empty"]*7)
            )
            connect.commit()
            print(f"Was added the new user with id -{id_user}")
        print(f"We have this user, his id - {id_user}")
        
def delete_data(id_user: int) -> None:
    """Deleting from the db"""
    with sqlite3.connect("bot_users.db") as connect:
    
        cursor = connect.cursor()

        cursor.execute(
            'DELETE FROM plans WHERE id_users=?', (id_user,))

        connect.commit()





# async def main():

#     await connect_db()

    
    
#     res = await get_data_user(923610747, "tu")
#     print(*res)
#     print("-"*10)
#     res2 = await get_data_user(923610747, "mn")
#     print(*res2)


# asyncio.run(main())