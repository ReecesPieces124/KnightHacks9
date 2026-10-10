import discord
from data import json_manager

leaderboard_enabled : bool
leaderboard_channel_name : str
leaderboard_users_displayed : int

leaderboard_user_points : bool
leaderboard_user_deaths : bool
leaderboard_pebbles: bool

# ////////////////////////////////////////////////////////////////////////////////////

async def update_leaderboard(message : discord.Message):

    if not leaderboard_enabled:
        return

    from addons.fun import games
    from addons.fun import misc

    # ---------------------------------------------------------------------------

    # TEXT DISPLAY

    text : str = "LEADERBOARD:\n"

    # POINTS
    if leaderboard_user_points:
        data = json_manager.get_json_var(message.channel.guild.id, games.points_key) or {}
        top = sorted(data.items(), key=lambda item: item[1], reverse=True)[:10]

        text += "\n-//=============== POINTS ===============//-\n\n"
        for index, (user_id, value) in enumerate(top):
            text += f"\t{index + 1} ) <@{user_id}> : {value}\n"

    # DEATHS
    if leaderboard_user_points:
        data = json_manager.get_json_var(message.channel.guild.id, games.deaths_key) or {}
        top = sorted(data.items(), key=lambda item: item[1], reverse=True)[:leaderboard_users_displayed]

        text += "\n-//=============== DEATHS ===============//-\n\n"
        for index, (user_id, value) in enumerate(top):
            text += f"\t{index + 1} ) <@{user_id}> : {value}\n"

    if leaderboard_pebbles:
        data = json_manager.get_json_var(message.channel.guild.id, misc.pebble_key) or {}
        top = sorted(data.items(), key=lambda item: item[1].get(misc.pebble_key_count_key, 0), reverse=True)[:leaderboard_users_displayed]

        text += "\n-//============== PEBBLES ===============//-\n\n"
        for index, (user_id, value) in enumerate(top):
            count = value.get(misc.pebble_key_count_key, 0)
            text += f"\t{index + 1} ) <@{user_id}> : {count}\n"

    # ---------------------------------------------------------------------------

    # CHANNEL AND MESSAGE MANAGER

    # GET LEADERBOARD MESSAGE AND UPDATE
    data = json_manager.get_json_var(message.channel.guild.id, "leaderboard_id") or []

    channel_id : int = 0
    message_id : int = 0
    if len(data) == 2:
        channel_id = data[0]
        message_id = data[1]

    try:
        leaderboard_channel : discord.channel
        leaderboard_message : discord.Message
        data_updated: bool = False

        # GET CHANNEL
        try:
            leaderboard_channel = await message.guild.fetch_channel(channel_id)
        except:
            data_updated = True
            # CREATE CHANNEL
            server = message.guild
            channel = await server.create_text_channel(leaderboard_channel_name, )
            channel_id = channel.id
            # LOCK CHANNEL
            await channel.set_permissions(message.guild.default_role, send_messages=False)
            # GET REFERENCE
            leaderboard_channel = await message.guild.fetch_channel(channel_id)

        # GET MESSAGE
        try:
            leaderboard_message = await leaderboard_channel.fetch_message(message_id)
        except:
            data_updated = True
            # CREATE MESSAGE
            message_id = (await leaderboard_channel.send(text)).id
            # GET REFERENCE
            leaderboard_message = await leaderboard_channel.fetch_message(message_id)

        # SAVE DATA
        if data_updated:
            json_manager.set_json_var(message.channel.guild.id, "leaderboard_id",
                                      [channel_id, message_id])

        # UPDATE LEADERBOARD
        await leaderboard_message.edit(content = text)

    except:
        pass
        #await message.channel.send("I do not have permissions to create leaderboard :(")

# ////////////////////////////////////////////////////////////////////////////////////
