from array import ArrayType

import discord
import random
import re
import datetime
import sys

import data.json_manager as json_manager
from addons.fun import games
from addons.fun import leaderboard

# ////////////////////////////////////////////////////////////////////////////////////

# MARRY ME

spouse_role : str

async def marry(message : discord.Message):

    role = discord.utils.get(message.guild.roles, name=spouse_role)
    if role is None:
        role = await message.guild.create_role(name=spouse_role, color=discord.Color.from_rgb(255,182,193), hoist=True)

    if role in message.author.roles:
        await message.reply("Give someone else a chance")
        return

    try:
        for m in role.members:
            await m.remove_roles(role)

        await message.author.add_roles(role)

        await message.reply(f"<@{message.author.id}> and I are now happily married!")

    except:
        await message.reply(f"Nah")

# ////////////////////////////////////////////////////////////////////////////////////

# TIMEOUT

timeout_exceptions = []
timeout_ignore_spouse : bool
timeout_exception_message : str

timeout_random_range = (1, 3)
timeout_targeted_range = (5, 8)
timeout_self_target_time : int
timeout_multiplier : int

async def user_timeout(message : discord.Message, client : discord.Client):

    match = re.search(r'<@(\d+)>', message.content.lower())

    if not match: # RANDOM MUTE

        all_users = message.channel.guild.members
        random_user = random.choice(all_users)
        random_num: int = random.randint(timeout_random_range[0], timeout_random_range[1])
        random_num_multiplied = random_num * timeout_multiplier

        # TIMEOUT RANDOM USER
        try:
            await random_user.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=random_num), reason="bad luck")
            await message.channel.send(f"Random user <@{random_user.id}> has been muted for {random_num} minutes.")
        except:
            await message.channel.send(f"<@{random_user.id}>, CANNOT BE MUTED")
            print("Cannot mute target")
            sys.stdout.flush()

        # TIMEOUT AUTHOR
        try:
            await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=random_num_multiplied), reason=f"YOU DID THIS TO YOURSELF")
            await message.channel.send(f"In exchange <@{message.author.id}> has been muted for {random_num_multiplied} minutes")
        except:
            print("Cannot mute author")
            sys.stdout.flush()

    else: # TARGETED MUTE

        target_user = await message.channel.guild.fetch_member(match.group(1))
        random_num: int = random.randint(timeout_targeted_range[0], timeout_targeted_range[1])
        random_num_multiplied: int = random_num * timeout_multiplier

        if timeout_ignore_spouse:
            married_role = discord.utils.get(message.guild.roles, name=spouse_role)
            if married_role in target_user.roles:
                await message.reply("I WOULD NEVER DO THAT TO MY SPOUSE")
                return


        # TARGET IS SUICIDAL
        if target_user.id == message.author.id:
            try:
                await message.channel.send(f"Dude are u ok???\n<@{message.author.id}> has been muted for {timeout_self_target_time} minutes" )
                await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=timeout_self_target_time), reason=f"Self harm")
            except:
                print("Cannot mute author")
                sys.stdout.flush()

        # TARGET IS EXCEPTION OR BOT
        elif target_user.id  in timeout_exceptions and client.user.id  in timeout_exceptions:
            try:
                await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=random_num_multiplied), reason=f"YOU DID THIS TO YOURSELF")
                await message.channel.send(f"NICE TRY STUPID\n<@{message.author.id}> has been muted for {random_num_multiplied} minutes")
            except:
                print("Cannot mute author")
                sys.stdout.flush()

        # NORMAL TARGETED TIMEOUT
        else:

            # TIMEOUT TARGET
            try:
                await target_user.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=random_num), reason=f"<@{message.author.id}>")
                await message.channel.send(
                    f"<@{target_user.id}> has been muted for {random_num} minutes")
            except:
                await message.channel.send(f"<@{target_user.id}>, CANNOT BE MUTED")
                print("Cannot mute target")
                sys.stdout.flush()

            #TIMEOUT AUTHOR
            try:
                await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=random_num_multiplied), reason=f"YOU DID THIS TO YOURSELF")
                await message.channel.send(
                    f"In exchange <@{message.author.id}> has been muted for {random_num_multiplied} minutes")
            except:
                print("Cannot mute author")
                sys.stdout.flush()


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

# CHEESE TOUCH

cheese_touch_role : str

async def cheese_touch(message : discord.Message):
    target : discord.Member = None
    match = re.search(r'<@(\d+)>', message.content.lower())
    if match:
        target = await message.channel.guild.fetch_member(match.group(1))

    # NO TARGET FOUND
    if not target:
        await message.channel.send("@someone to target them with the cheese touch")
        return

    if target.bot:
        await message.reply("I'm afraid I can't do that, Dave")
        return

    if target.id == message.author.id:
        await message.reply("????????? is this how you get you sick kicks?????")
        return


    # CREATE ROLE IF IT DOES NOT EXIST
    role = discord.utils.get(message.guild.roles,name=cheese_touch_role)
    if role is None:
        role = await message.guild.create_role(name=cheese_touch_role, color=discord.Color.gold(), hoist=True)

    # IF ROLE EMPTY, OR USER HAS ROLE, TOUCH CHEESE
    if role in message.author.roles or len(role.members) <= 0:

        # add role to touched
        try:
            await target.add_roles(role)
            await message.channel.send(f"<@{target.id}> NOW HAS THE CHEESE TOUCH. EVERYONE SOCIALLY ISOLATE THEM")

            try:
                await message.author.remove_roles(role)
            except:
                await message.reply(f"If you are reading this message, you still have the touch for some reason")
        except:
            await message.reply(f"IDK why but they are immune to the cheese touch")

    # IF USER DOES NOT HAVE ROLE FAIL
    else:
        await message.reply(f"you do not have the cheese touch my friend")


# ////////////////////////////////////////////////////////////////////////////////////

# PEBBLE

pebble_key : str
pebble_key_count_key : str
pebbles_have_cost : bool
pebble_cost : int

pebble_types = {
    'Common': ["blue_circle", "red_circle", "yellow_circle", "green_circle", "purple_circle"],
    'Rare': ["large_blue_diamond", "small_blue_diamond", "large_orange_diamond", "small_red_triangle_down", "small_red_triangle"],
    'Square': ["blue_square", "red_square", "yellow_square", "green_square", "purple_square"],
    'Heart': ["blue_heart", "red_heart", "yellow_heart", "green_heart", "purple_heart"],
    'Ball': ["yarn", "softball", "yo_yo", "tennis", "crystal_ball"],
    'Fruit': ["blueberries", "lemon", "apple", "kiwi", "grapes"],
    'Animal': ["jellyfish", "hatched_chick", "crab", "snake", "bug"],
    'Legendary': ["gem", "coin", "dollar"],
    'WHITE': ["white_circle", "white_large_square", "white_heart", "egg", "mouse2"],
    'BLACK': ["black_circle", "black_large_square", "black_heart", "8ball", "black_cat"]
}
pebble_weights= {
    'Common': 1000,
    'Rare': 250,
    'Square': 100,
    'Heart': 100,
    'Ball': 100,
    'Fruit': 100,
    'Animal': 100,
    'Legendary': 50,
    'WHITE': 20,
    'BLACK': 10,
}
total_weight = sum(pebble_weights.values())

def get_pebble() -> str:
    chosen_category = random.choices(
        population=list(pebble_weights.keys()),
        weights=list(pebble_weights.values()),
        k=1)[0]
    #result : str = random.choice(pebble_types[chosen_category])
    result : str = pebble_types[chosen_category][random.randint(0, len(pebble_types[chosen_category]) - 1)]
    return result

async def pebble(message : discord.Message):
    target : discord.Member = None

    match = re.search(r'<@(\d+)>', message.content.lower())
    if match:
        target = await message.channel.guild.fetch_member(match.group(1))

    # NO TARGET FOUND
    if not target:
        await message.reply("@ Someone to send them a pebble")
        return

    # TARGET IS SELF
    if target.id == message.author.id:
        await message.reply("This is sad to watch")
        return

    # CHARGE FOR PEBBLE
    if pebbles_have_cost:
        data: dict = json_manager.get_json_var(message.channel.guild.id, games.points_key) or {}
        user_points = data.get(str(message.author.id), 0) - pebble_cost

        if user_points < 0:
            try:
                await message.reply(f"YOU ARE TOO POOR.\n\nTHE PRICE OF A PEBBLE IS {pebble_cost} POINTS")
            except:
                pass
            return

        data[str(message.author.id)] = user_points
        json_manager.set_json_var(message.channel.guild.id, games.points_key, data)

    # ADD PEBBLE TO SAVE FILE
    new_pebble : str = get_pebble()

    data: dict = json_manager.get_json_var(message.channel.guild.id, pebble_key) or {}
    target_pebbles = data.get(str(target.id), {})
    target_pebbles[new_pebble] =  target_pebbles.get(new_pebble, 0) + 1
    target_pebbles[pebble_key_count_key] =  target_pebbles.get(pebble_key_count_key, 0) + 1
    data[str(target.id)] = target_pebbles
    json_manager.set_json_var(message.channel.guild.id, pebble_key, data)

    try:
        await message.channel.send(f"<@{message.author.id}> gifted <@{target.id}> a pebble for {pebble_cost} points!\
                                   \n\n:{new_pebble}: added to <@{target.id}>'s collection!")
        await leaderboard.update_leaderboard(message)

    except:
        pass


async def collection(message : discord.Message):
    target: discord.Member = message.author

    match = re.search(r'<@(\d+)>', message.content.lower())
    if match:
        target = await message.channel.guild.fetch_member(match.group(1))

    data: dict = json_manager.get_json_var(message.channel.guild.id, pebble_key) or {}
    user_pebbles : dict = data.get(str(target.id), {})
    text = f"\n\n<@{target.id}>'s COLLECTION:\n\n"

    for key in pebble_types.keys():
        if key == pebble_key_count_key:
            continue

        if set(pebble_types[key]) & set(user_pebbles):
            text += f"**{key.upper()}** : \n"
        else:
            text += f"UNDISCOVERED : \n"

        # LIST PEBBLES
        for pebb in pebble_types[key]:
            peb_count = user_pebbles.get(pebb, 0)
            if peb_count != 0:
                text += f"| :{pebb}: = {peb_count} "
            else:
                text += f"| :grey_question: "
        text += "\n"


    text += "\n@someone to gift them a pebble!\n"

    await message.channel.send(text)




market_key : str

async def market(message : discord.Message):
    target: discord.Member = None

    match = re.search(r'<@(\d+)>', message.content.lower())
    if match:
        target = await message.channel.guild.fetch_member(match.group(1))


    return





# ////////////////////////////////////////////////////////////////////////////////////


lock_in_time : int = 60

async def lock_in(message : discord.Message):
    try:
        await message.author.timeout(discord.utils.utcnow() + datetime.timedelta(minutes=lock_in_time), reason="locked in")
        await message.channel.send(f"<@{message.author.id}> is locking in for {lock_in_time} minutes.")
    except:
        await message.reply(f"You are too powerful to be muted")


# ////////////////////////////////////////////////////////////////////////////////////

# DOXX

import faker

async def doxx(message : discord.Message):
    fake = faker.Faker()

    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    lat = round(random.uniform(-90, 90), 4)
    lon = round(random.uniform(-180, 180), 4)
    ipv6 = f"fe80::{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}:{random.randint(0, 65535):x}"
    mac = ':'.join([''.join([random.choice('0123456789ABCDEF') for _ in range(2)]) for _ in range(6)])
    dns = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    alt_dns = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    gateway = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    subnet = f"255.255.{random.randint(0, 255)}.{random.randint(0, 255)}"
    open_ports = f"{random.randint(1, 65535)},{random.randint(1, 65535)}"
    hops = f"192168.0.1 192168.1.1 {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'} host-{random.randint(1, 255)}.{random.randint(1, 255)}.ucom.com {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}"
    services = [
        f"[HTTP] {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:80=>{f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:80",
        f"[HTTP] {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:443=>{f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:443",
        f"[UDP] {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:788=>{f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:6557",
        f"[TCP] {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:67891=>{f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:345",
        f"[TCP] {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:7777=>{f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:7778",
        f"[TCP] {f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:898=>{f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'}:667"
    ]

    info = f"""
IP: {ip}
N: {lat}
W: {lon}
SS Number: {random.randint(1000000000000000, 9999999999999999)}
IPv6: {ipv6}
Enabled DMZ: {f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"}
MAC: {mac}
ISP: {fake.company()}
Universal DNS: {dns}
ALT DNS: {alt_dns}
Dlink WAN: {f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"}
GATEWAY: {gateway}
SUBNET MASK: {subnet}
UDP OPEN PORTS: {open_ports}
TCP OPEN PORTS: {open_ports}
ROUTER VENDOR: {fake.company()}
DEVICE VENDOR: WIN32-X
CONNECTION TYPE: Ethernet
ICMP HOPS: {hops}
TOTAL HOPS: 8
ACTIVE SERVICES: {', '.join(services)}
EXTERNAL MAC: {':'.join([''.join([random.choice('0123456789ABCDEF') for _ in range(2)]) for _ in range(6)])}
MODEM JUMPS: {random.randint(1, 100)}
    """

    await message.channel.send(info)



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


# ////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////