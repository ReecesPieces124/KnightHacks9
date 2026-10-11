import discord
import re
from enum import Enum
import random
import time

# ////////////////////////////////////////////////////////////////////////////////////

# WHO COOLDOWN
# Each user can only trigger the who command once every who_cooldown_minutes.
# Tracked per invoking user (in-memory, resets on restart).
who_cooldown_minutes : int = 10
who_last_used : dict = {}

# GET RANDOM USER
async def random_user(message : discord.Message):
    # ON COOLDOWN -> FALL THROUGH TO THE DEFAULT RESPONSE
    now = time.monotonic()
    if message.author.id in who_last_used and now - who_last_used[message.author.id] < who_cooldown_minutes * 60:
        return False
    who_last_used[message.author.id] = now

    all_users = message.channel.guild.members
    random_user = random.choice(all_users)
    await message.channel.send(f"<@{random_user.id}>")

