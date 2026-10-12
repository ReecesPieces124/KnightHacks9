import os
from dotenv import load_dotenv

version : str = "1.0.2"

# TOKEN
load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))

# CHANNEL BLACKLIST
blacklisted_channels = {}
bl_str = os.getenv('BLACKLISTED_CHANNELS', '')
if bl_str:
    for entry in bl_str.split(';'):
        if ':' not in entry:
            continue
        guild_s, chan_s = entry.split(':', 1)
        guild_s, chan_s = guild_s.strip(), chan_s.strip()
        try:
            guild_id = int(guild_s)
        except ValueError:
            continue
        try:
            blacklisted_channels[guild_id] = [int(x.strip()) for x in chan_s.split(',') if x.strip()]
        except ValueError:
            pass

# ////////////////////////////////////////////////////////////////////////////////////

# SETTINGS
print_input : bool = True # Will output all received messages to terminal
print_unrelevant : bool = False # Will output relevant received messages to terminal
print_response : bool = True # Will output bot response

no_trigger : bool = False # Bot will respond to all messages
case_sensitive : bool = False # Response triggers words are case-sensitive

# ////////////////////////////////////////////////////////////////////////////////////

# ADDONS









import topics.fun.misc as misc


misc.timeout_exceptions = [760164196125507605, ]# user ids of users that cant be timed out
misc.timeout_exception_message = "NICE TRY STUPID" # Message sent when someone triggers an exception
