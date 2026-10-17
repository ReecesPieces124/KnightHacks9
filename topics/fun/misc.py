from array import ArrayType

import discord
import random
import datetime
import re

import data.json_manager as json_manager

# ////////////////////////////////////////////////////////////////////////////////////

# NERD
async def nerd(message : discord.Message):
    text: str
    if message.reference:
        reference = await message.channel.fetch_message(message.reference.message_id)
        text = ''.join(random.choice([c.lower(), c.upper()]) for c in reference.content)
    else:
        text: str = ''.join(random.choice([c.lower(), c.upper()]) for c in message.content)

    await message.channel.send("\"" + text + "\" - :nerd:")

# ////////////////////////////////////////////////////////////////////////////////////

# LOCK IN

async def lock_in(message : discord.Message):
    content = message.content if message.content else ""
    hours = 1
    m = re.search(r'\block in\b\s+(\d+)\b', content)
    if m:
        try:
            h = int(m.group(1))
            if 1 <= h <= 8:
                hours = h
        except ValueError:
            hours = 1
    minutes = hours * 60
    try:
        await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=minutes), reason="locked in")
        unit = "hour" if hours == 1 else "hours"
        await message.channel.send(f"<@{message.author.id}> is locking in for {hours} {unit}.")
    except Exception:
        await message.reply(f"You are too powerful to be muted")


# ////////////////////////////////////////////////////////////////////////////////////

# QUOTE

quote_key : str = "quotes"

async def quote(message : discord.Message):

    # IS RESPONSE
    if message.reference is not None:
        quote_message = await message.channel.fetch_message(message.reference.message_id)
        quote = (quote_message).content

        data : list = json_manager.get_json_var(message.channel.guild.id, quote_key) or []
        data.append([quote_message.author.id, quote])
        json_manager.set_json_var(message.channel.guild.id, quote_key, data)

        await quote_message.reply("Gerbot will remember that.")

    else:
        data: list = json_manager.get_json_var(message.channel.guild.id, quote_key) or []
        random_quote = random.choice(data or [[]])

        if random_quote:
            await message.channel.send('"' + random_quote[1] + f'" - <@{random_quote[0]}>')
        else:
            await message.channel.send("No quotes yet, reply to someones message and use the quote command to quote them")


#add funnction to differenitate if a use wants practice problems from a specific topic


# ////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////