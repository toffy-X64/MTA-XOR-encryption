from encrypt import *
from file_hander import *

from sys import stdout
import numpy as np

import asyncio, logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


class Commands:

    def __init__(self):
        self.cmd_list = [
            ["start", self.command_start],
            ["random", self.command_random],
            ["enc", self.command_encrypt]
        ]
        self.fileHandler = FileHandler()
        self.waiting_clients = []

    async def command_start(self, message: Message, bot: Bot):
        await message.answer(f"Hello {hbold(message.from_user.full_name)} \nEnter `/enc` to encrypt your .lua File")

    async def command_random(self, message: Message, bot: Bot):
        await message.answer(f"Hello random")

    async def command_encrypt(self, message:Message, bot: Bot):
        await message.answer(f"Send your .lua file here!")
        user_id = message.from_user.id

        # np_array = np.array(self.waiting_clients)
        # result = np.where(np_array == user_id)
        
        # if result[0].size <= 0:
        #     self.waiting_clients.append(user_id)