from array import ArrayType

import discord
import random
import datetime

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

lock_in_time : int = 60

async def lock_in(message : discord.Message):
    try:
        await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=lock_in_time), reason="locked in")
        await message.channel.send(f"<@{message.author.id}> is locking in for {lock_in_time} minutes.")
    except:
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