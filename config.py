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

import addons.fun.leaderboard as lead

lead.leaderboard_enabled : bool = True
lead.leaderboard_channel_name = "leaderboard" # The name of the channel the leaderboard will be in
lead.leaderboard_users_displayed = 5 # Number of users displayed for each rank

lead.leaderboard_user_points = True # Display top user by points in leaderboard
lead.leaderboard_user_deaths = True # Display top user by deaths in leaderboard
lead.leaderboard_pebbles = True # Display top user by pebbles



import addons.fun.games as games

games.roulette_count_points = True
games.roulette_count_deaths = True
games.roulette_kick = True
games.roulette_rejoin = True

games.cards_drawn  = 4
games.card_images_folder = "files/img/cards"
games.cards_points_enabled = True



import addons.fun.rps as rps

rps.rps_track_wins = True # keep track of wins
rps.rps_points = True # use conventional point system
rps.rps_win_points = 10 # points awarded


import addons.fun.misc as misc

misc.spouse_role = "HAPPILY MARRIED"
misc.cheese_touch_role = "CHEESE TOUCH"

misc.timeout_exceptions = [760164196125507605, ]# user ids of users that cant be timed out
misc.timeout_ignore_spouse = True # if true, will not time out spouse
misc.timeout_exception_message = "NICE TRY STUPID" # Message sent when someone triggers an exception
misc.timeout_random_range = (1, 3) # the range of numbers that a random timeout can be
misc.timeout_targeted_range = (5, 8) # the range of numbers that a targeted timeout can be
misc.timeout_self_target_time = 10
misc.timeout_multiplier = 2 # the punishment multiplier for timeing out

misc.pebble_key = "pebbles"
misc.pebble_key_count_key = "count"
misc.pebbles_have_cost = True
misc.pebble_cost = 10