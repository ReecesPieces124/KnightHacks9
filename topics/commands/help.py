import discord

import config

# ////////////////////////////////////////////////////////////////////////////////////

# SLIDE TOPICS THE BOT RECOGNIZES
topic_names : tuple = (
    "linked list",
    "binary tree",
    "avl tree",
    "hash table",
    "heap",
    "queue",
    "stack",
    "trie",
    "recurrence relation",
    "recursion",
    "dma",
    "c review",
    "base conversion",
    "algorithm analysis",
    "sorting",
)

# ////////////////////////////////////////////////////////////////////////////////////

# SEND THE HELP EMBED
async def help_command(message : discord.Message, client : discord.Client):
    embed = discord.Embed(
        title = "TAbot Commands",
        description = "Start with **ta**, then a command. Example: `ta linked list`",
        color = discord.Color.gold(),
    )

    embed.add_field(
        name = "Study",
        value = (
            "`<topic>` — send that topic's slides\n"
            "`<topic> practice` — a random practice problem for that topic\n"
            "`practice` — a random practice problem from any topic"
        ),
        inline = False,
    )

    embed.add_field(
        name = "Topics",
        value = "  ·  ".join(f"`{name}`" for name in topic_names),
        inline = False,
    )

    embed.add_field(
        name = "Schedule",
        value = (
            "`next quiz` — the next quiz\n"
            "`next exam` — the next test or exam"
        ),
        inline = False,
    )

    embed.add_field(
        name = "Fun & Tools",
        value = (
            "`who` — ping a random student\n"
            "`nerd` — NeRD-IfY a message, or reply to one to nerd-ify that\n"
            "`lock in` — timeout yourself so you can focus\n"
            "`motivate` — a motivational push\n"
            "`react` — a random reaction image"
        ),
        inline = False,
    )

    if client is not None and client.user is not None:
        embed.set_footer(text = f"TAbot v{config.version}", icon_url = client.user.display_avatar.url)

    await message.channel.send(embed = embed)
