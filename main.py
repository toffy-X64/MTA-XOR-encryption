from config_data import TOKEN
from Ibot import *


if __name__ == "__main__":
    TgBot = IBot(TOKEN)
    asyncio.run(TgBot.run())