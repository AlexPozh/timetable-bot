from environs import Env

from pydantic import SecretStr

from dataclasses import dataclass

# init the Env class from environs to work with variable environment
env: Env = Env()


# read our variable environment
env.read_env()


# config class for Bot
@dataclass
class ConfigBot:
    bot_token: SecretStr


# config class for database
@dataclass
class ConfigDatabase:
    host: SecretStr
    user: SecretStr
    password: SecretStr
    db_name: SecretStr


Config_bot = ConfigBot(bot_token=env('BOT_TOKEN'))

Config_database = ConfigDatabase(
    host=env("HOST"),
    user=env("USER"),
    password=env("PASSWORD"),
    db_name=env("DB_NAME"))
# print(Config_bot.bot_token)