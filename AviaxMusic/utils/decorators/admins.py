# utils/decorators/admins.py

from typing import List, Union

from pyrogram.types import Message
from pyrogram.enums import ChatType

from config import SUDOERS
from AviaxMusic import app


def is_sudo_or_owner(user_id: int) -> bool:
    """Check if the user is a sudo user or the owner"""
    return user_id in SUDOERS


def adminsOnly(mystic):
    async def wrapper(client, message: Message):
        # Check if the user is a sudo user or the owner
        if message.from_user and is_sudo_or_owner(message.from_user.id):
            return await mystic(client, message)
        else:
            # Send a message indicating command is restricted
            await message.reply_text(
                "This command is restricted to sudo users and the bot owner only."
            )
            return
    return wrapper
