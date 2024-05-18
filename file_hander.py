from aiogram.types import Message, InputFile
from aiogram import Bot
from encrypt_file_gen import EncryptGenerator

from error_handler import ErrorHandler
import os

class FileHandler():

    def __init__(self):
        self.filesFolder = "files/"
        self.error_handler = ErrorHandler()
        self.enc_file_gen = EncryptGenerator()

    async def send_file(self, filePath, message: Message, bot: Bot):
        print(f"Sending file from path: {filePath}")
        if os.path.exists(filePath):
            with open(filePath, "rb") as file:
                await bot.send_document(chat_id=message.chat.id, document=InputFile(file, filename="File.lua"))
        else:
            await message.answer("Error path!")

    def check_file_by_statements(self, user_id, file):
        if not user_id or not file:
            return self.error_handler.return_error("File Handler Error #1")
        
    async def save_file(self, user_id, file, bot: Bot, message: Message):
        if not user_id or not file:
            return self.error_handler.return_error("File Handler Error #2")
        
        path = os.path.join(self.filesFolder, str(user_id))
        if not os.path.isdir(path):            
            os.makedirs(path, mode=0o666)

        path = os.path.join(path, str(message.message_id))
        os.makedirs(path)

        file_path = os.path.join(path, "File.lua")
        await bot.download_file(file.file_path, file_path)

        return self.error_handler.return_response(file_path)

    async def handle_document(self, message: Message, bot: Bot):
        document = message.document
        user_id = message.from_user.id
        if document:
            file_name = document.file_name
            file_extension = os.path.splitext(file_name)[1].lower()
            file_id = document.file_id

            if file_extension != ".lua":
                await message.answer("File must be .lua!")
                return

            if file_id and document:
                file = await bot.get_file(file_id)
                save_file = await self.save_file(user_id, file, bot, message)

                if not save_file["state"]:
                    await message.answer(save_file['data'])
                    return
                
                await message.answer("I received the file!")

                encryption_process = self.enc_file_gen.generateEncryptFile(save_file['data'], user_id)

                print(f"Encrypted file path: {encryption_process['data']}")
                await self.send_file(encryption_process["data"], message, bot)
                await message.answer(f"File sent: {encryption_process['data']}")
            else:
                await message.answer("Error in Telegram API")
        else:
            await message.answer("No document found in the message")

# Usage example (assuming you have message and bot objects)
# file_handler = FileHandler()
# await file_handler.handle_document(message, bot)
