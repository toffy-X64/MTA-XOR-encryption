from commands import *


class IBot(Commands):
    def __init__(self, token):
        super().__init__()
        self.dp = Dispatcher()
        self.token = token

    async def register_cmd(self):
        for cmd, handler in self.cmd_list:
            if cmd == "start":
                self.dp.message.register(self.command_start, CommandStart())
            else:
                self.dp.message.register(handler, Command(cmd))

    
    async def pre_handle_document(self, message: Message, bot: Bot):
        # user_id = message.from_user.id
        # np_array = np.array(self.waiting_clients)
        # result = np.where(np_array == user_id)
        # if result[0].size > 0:
        await self.fileHandler.handle_document(message, bot)
        

    async def register_handler(self):
        self.dp.message.register(self.pre_handle_document, lambda message: message.content_type == types.ContentType.DOCUMENT)
    
    async def run(self):
        logging.basicConfig(level=logging.INFO, stream = stdout)
        self.bot = Bot(self.token, parse_mode=ParseMode.HTML)
        await self.register_cmd()
        await self.register_handler()
        await self.dp.start_polling(self.bot)
