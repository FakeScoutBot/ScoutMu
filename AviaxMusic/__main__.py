# AviaxMusic/__main__.py

# Import the necessary modules
import asyncio
import importlib

from pyrogram import idle

from AviaxMusic import app, userbot
from AviaxMusic.core.call import Aviax
from AviaxMusic.misc import sudo
from AviaxMusic.plugins import ALL_MODULES
from AviaxMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # Load all modules
    print("𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐌𝐨𝐝𝐮𝐥𝐞𝐬...")
    for all_module in ALL_MODULES:
        importlib.import_module("AviaxMusic.plugins." + all_module)
    print("𝐀𝐥𝐥 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝!")

    # Start the userbot
    await userbot.start()
    print("𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝!")

    # Start the main bot
    await app.start()
    print("𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝!")

    # Call the main music player
    await Aviax.start()
    print("𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐒𝐭𝐚𝐫𝐭𝐞𝐝!")

    # Load banned users
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    print("𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲!")

    # Idle the bot
    await idle()
    print("𝐁𝐨𝐭 𝐒𝐭𝐨𝐩𝐩𝐞𝐝!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
