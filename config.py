import os
from dotenv import load_dotenv

version : str = "1.0.2"

# TOKEN
load_dotenv()
TOKEN = str(os.getenv('DISCORD_TOKEN'))

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
