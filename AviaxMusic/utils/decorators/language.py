from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.database import get_lang, is_maintenance
from config import SUPPORT_GROUP
from strings import get_string
from typing import Callable, Union
from pyrogram import Client
from pyrogram.types import Message, CallbackQuery
from AviaxMusic import app
from utils.decorators.admins import adminsOnly


def language(mystic: Callable) -> Callable:
    async def wrapper(client, message: Union[Message, CallbackQuery], *args, **kwargs):
        # Always apply the adminsOnly check first
        if isinstance(message, Message):
            if not message.from_user or not message.from_user.id:
                return await message.reply_text("You are not authorized to use this command.")
            
            # Check if the user is a sudo user or the owner
            from utils.decorators.admins import is_sudo_or_owner
            if not is_sudo_or_owner(message.from_user.id):
                return await message.reply_text(
                    "This command is restricted to sudo users and the bot owner only."
                )
        
        # If it's a callback query, check the user
        elif isinstance(message, CallbackQuery):
            if not message.from_user or not message.from_user.id:
                return await message.answer("You are not authorized to use this command.", show_alert=True)
            
            # Check if the user is a sudo user or the owner
            from utils.decorators.admins import is_sudo_or_owner
            if not is_sudo_or_owner(message.from_user.id):
                return await message.answer(
                    "This action is restricted to sudo users and the bot owner only.", 
                    show_alert=True
                )
        
        # If the user is authorized, proceed with the command
        return await mystic(client, message, *args, **kwargs)
    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
