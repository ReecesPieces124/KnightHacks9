
import random
import discord

possibilities = ['rock', 'paper', 'scissors', 'lizard', 'spock',
                     'mouse', 'worm', 'batman', 'snake', 'gun', 'knife',
                     'toyota corolla', 'sock', 'human', 'banana', 'airplane',
                     'bug', 'computer', 'fork', 'the mediterranean sea', 'shoe',
                     'cheeseburger', 'thermonuclear ballistic missile']
possible_games : dict = {
    ("paper", "rock") : "Paper beats rock!",
    ("rock", "scissors") : "Rock beats scissors!",
    ("rock", "lizard") : "Rock smashes lizard!",
    ("spock", "rock") : "Spock blasts rock",
    ("rock", "mouse") : "Rock smashes mouse!",
    ("rock", "worm") : "Rock obliterates worm!",
    ("batman", "rock") : "Dont even try that - Batman",
    ("snake", "rock") : "Snake eats rock!",
    ("gun", "rock") : "Never bring a rock to a gun fight.",
    ("knife", "rock") : "Knife slices rock",
    ("toyota corolla", "rock") : "Rock disintegrated the moment it is hit at 90mph",
    ("sock", "rock") : "Sock eats rock and becomes rock in a sock",
    ("rock", "human") : "*OW!*",
    ("rock", "banana") : "*SPLAT*",
    ("rock", "airplane") : "Rock gets stuck in airplanes turbine",
    ("rock", "bug") : "Crushed like a bug in the ground",
    ("rock", "computer") : "MY MONITOR",
    ("fork", "rock") : "Yummy rock mmmmm",
    ("the mediterranean sea", "rock") : "WHERE IS THE ROCK I DONT SEE IT",
    ("shoe", "rock") : "Rock is kicked into the stratosphere",
    ("rock", "cheeseburger") : "I WAS GOING TO EAT THAT",
    ("scissors", "paper") : "Scissors beat paper!",
    ("lizard", "paper") : "Lizard eats paper",
    ("paper", "spock") : "Spock gets a paper cut, which becomes infected and kills him",
    ("mouse", "paper") : "Mouse eats paper",
    ("worm", "paper") : "Worm waits for paper to decompose and eats it i guess",
    ("paper", "batman") : "Its a picture of batman's parents. He dies of sadness",
    ("snake", "paper") : "Snake uses paper to make plane and fly.",
    ("gun", "paper") : "I was a close one for sure",
    ("knife", "paper") : "The knife is from a knife sharpening youtube channel",
    ("toyota corolla", "paper") : "Paper was turned into confetti",
    ("paper", "sock") : "It was anyone's game really",
    ("human", "paper") : "Human uses paper to file taxes and make financially sound investments, strengthening their portfolio and increasing their total networth!",
    ("paper", "banana") : "Paper wrapped around banana and made it ripe",
    ("airplane", "paper") : "Paper airplane vs real airplane",
    ("paper", "bug") : "Paper was used to pick up bug and flush it down the toilet!",
    ("paper", "computer") : "Wait, SpongeBob! We're not cavemen! We have technology!",
    ("fork", "paper") : "MMMM, yummy paper",
    ("the mediterranean sea", "paper") : "It was a close one for sure",
    ("paper", "shoe") : "Paper killed shoe with extreme violence",
    ("cheeseburger", "paper") : "Paper served as a helpful wrapper",
    ("scissors", "lizard") : "Snip Snip",
    ("spock", "scissors") : "They were safety scissors unfortunately",
    ("scissors", "mouse") : "That was kinda messed up if im honest",
    ("worm", "scissors") : "There are now two worms oh god",
    ("batman", "scissors") : "Its not safe to run with scissors kids- Batman",
    ("snake", "scissors") : "There are now two snakes oh god",
    ("gun", "scissors") : "Who thought that this would be a fair fight",
    ("scissors", "knife") : "Its like 2 knives in one",
    ("scissors", "toyota corolla") : "Slashed its tires",
    ("scissors", "sock") : "MY FAVORITE SOCK WHYYY",
    ("scissors", "human") : "bALD",
    ("scissors", "banana") : "Enjoy your Fruit salad",
    ("airplane", "scissors") : "I am already regretting adding a quip for every matchup its 2 am why do i do these things to myself i am so tired",
    ("scissors", "bug") : "BUGGY WHAT DID THEY DO TO YOU",
    ("computer", "scissors") : "ctrl-z",
    ("scissors", "fork") : "They are evenly matched I dont care who wins",
    ("the mediterranean sea", "scissors") : "???? how would this work",
    ("scissors", "shoe") : "Add holes to your shoes for proper airflow",
    ("scissors", "cheeseburger") : "The worst way to cut it in half",
    ("lizard", "spock") : "Spock dies from his deadly allergy to lizard poison",
    ("mouse", "lizard") : "I feel like a mouse would win",
    ("lizard", "worm") : "D:",
    ("batman", "lizard") : "The lizard now has 17 fractures, internal bleeding, a collapsed lung and failing kidneys but is not dead",
    ("lizard", "snake") : "A lizard is like a snake++",
    ("lizard", "gun") : "Lizard regenerates too quickly",
    ("lizard", "knife") : "Lizard regenerates its body parts",
    ("lizard", "toyota corolla") : "Lizard works at the DMV and canceled the cars drivers licence",
    ("sock", "lizard") : "Lizard is kinda op so this should balance it",
    ("lizard", "human") : "A lizard attacked me in the shower once and it won so im guessing this would play about the same.",
    ("lizard", "banana") : "Lizard gains extra potassium",
    ("airplane", "lizard") : "*Plane crash sound effect*",
    ("lizard", "bug") : "tasty",
    ("computer", "lizard") : "Lizard gets canceled on twitter",
    ("fork", "lizard") : "I would eat that thing",
    ("lizard", "the mediterranean sea") : "Lizard actually knows how to swim",
    ("shoe", "lizard") : "Stompity stomp stomp",
    ("cheeseburger", "lizard") : "Lizard burger",
    ("spock", "mouse") : "Spock eats that thing raw like a snickers bar",
    ("spock", "worm") : "Spock consumes it for protein",
    ("batman", "spock") : "It was an epic battle but I wont explain what happened",
    ("spock", "snake") : "Spock slurps it whole like a spaghetti",
    ("gun", "spock") : "Spock underestimated the 2nd amendment",
    ("spock", "knife") : "I imagine spock knows how to fight idk i dont watch star wars",
    ("toyota corolla", "spock") : "Spock is flattened into a fine paste",
    ("spock", "sock") : "spock wins by a p",
    ("spock", "human") : "I dont know I still haven't seen Dune",
    ("spock", "banana") : "Delicious and rich in potassium, and bananas are good for you as well",
    ("airplane", "spock") : "Spock fears air travel",
    ("bug", "spock") : "Spock thought the bug was icky",
    ("spock", "computer") : "Computer, deactivate Iguana",
    ("spock", "fork") : "Spork",
    ("the mediterranean sea", "spock") : "Spock forgot his pool noodle",
    ("spock", "shoe") : "Spock ate the shoe",
    ("spock", "cheeseburger") : "Spock put the hamburger on his feet",
    ("worm", "mouse") : "The mouse now has worms",
    ("batman", "mouse") : "Batman curb stomps the mouse",
    ("snake", "mouse") : "Pretty iconic match-up",
    ("mouse", "gun") : "Oh god the mouse has a glock",
    ("knife", "mouse") : "Kinda expected",
    ("mouse", "toyota corolla") : "The mouse has his drivers licence",
    ("mouse", "sock") : "A cozy home for the mouse",
    ("mouse", "human") : "Tell me about the rabbits George.",
    ("banana", "mouse") : "Its a known fact all mice are scared of bananas",
    ("airplane", "mouse") : "WOW WHO COULD HAVE EXPECTED THAT",
    ("mouse", "bug") : "yay",
    ("computer", "mouse") : "A classic duo",
    ("fork", "mouse") : "So delicious mmmmmmmmmmmm",
    ("the mediterranean sea", "mouse") : "Who did you THINK was gonna win",
    ("mouse", "shoe") : "You created a tap dancing mouse",
    ("cheeseburger", "mouse") : "Cheeseburger with extra protein",
    ("worm", "batman") : "I did not expect that one",
    ("snake", "worm") : "The prequel vs the sequel",
    ("gun", "worm") : "Oh no a worms 1 weakness",
    ("worm", "knife") : "NOW THERE ARE 2 OF THEM",
    ("worm", "toyota corolla") : "I feel bad for the work so it can win",
    ("worm", "sock") : "Inanimate object vs barely animate object",
    ("worm", "human") : "Parasite acquired!",
    ("worm", "banana") : "Fun fact, an estimated 75%-85% of all bananas are infested with small white worms in them known as Cavendish Parasites, which most people consume without even noticing due to the color of the worms.",
    ("airplane", "worm") : "Worm was caught smoking in the bathroom",
    ("worm", "bug") : "Which is better to find under the rock during recess?",
    ("worm", "computer") : "Oh god the worm deleted system 32.",
    ("fork", "worm") : "tasty worm surprise",
    ("worm", "the mediterranean sea") : "There is probably at least 1 worm in the mediterranean sea right now",
    ("worm", "shoe") : "Dont oyu hate it when you put on your shoe and its full to the brim with live worms am i right",
    ("worm", "cheeseburger") : "Worms eat cheeseburgers in their natural habitat i think",
    ("batman", "snake") : "Batman would wipe the floor with a snake",
    ("batman", "gun") : "I mean cmon this was not fair",
    ("batman", "knife") : "There was no way knife won",
    ("toyota corolla", "batman") : "Toyota corolla hits batman while going 99mph",
    ("batman", "sock") : "??? who comes up with these matchups",
    ("batman", "human") : "Batman broke all his bones and ruptured several internal oragans",
    ("banana", "batman") : "Batman chokes to death",
    ("airplane", "batman") : "Airplane wins with no explanation as to why",
    ("bug", "batman") : "The bug is a wasp",
    ("batman", "computer") : "Alt-f4 on your pc for a secret setting",
    ("fork", "batman") : "Batman was eaten",
    ("the mediterranean sea", "batman") : "Batman forgor how to swim",
    ("batman", "shoe") : "Batman has cooler shoes",
    ("cheeseburger", "batman") : "Batman's arteries clog and he dies at 60",
    ("snake", "gun") : "The snake now has a gun",
    ("snake", "knife") : "The snake now has a knife and a taste for human blood",
    ("toyota corolla", "snake") : "The snake is turned into roadkill. Is anyone gonna eat that.",
    ("sock", "snake") : "The snake spontaneously combusts at the sight of the sock",
    ("human", "snake") : "Steve Irwin to the rescue",
    ("banana", "snake") : "Snake is winning to many fights so im nerfing it",
    ("snake", "airplane") : "Snake watched top gun",
    ("snake", "bug") : "Snake bug snake bug who cares",
    ("snake", "computer") : "My favorite video game",
    ("fork", "snake") : "Green spaghetta",
    ("snake", "the mediterranean sea") : "Sea snake moment",
    ("shoe", "snake") : "Stompy stomp stomped",
    ("cheeseburger", "snake") : "Snakeburger",
    ("gun", "knife") : "Never bring a... Dont use a... What was it?",
    ("toyota corolla", "gun") : "nah",
    ("gun", "sock") : "How would a fight like this even work",
    ("gun", "human") : "Human would have won if it didn't need its blood or internal organs",
    ("banana", "gun") : "Banana wins because why not i guess",
    ("airplane", "gun") : "It takes more than a chunk of lead to take down a boeing 737",
    ("gun", "bug") : "???? isn't that overkill",
    ("gun", "computer") : "Wierd way to shut down a pc",
    ("fork", "gun") : "Fork jammed itself in guns chamber",
    ("gun", "the mediterranean sea") : "DIE INFERIOR OCEAN",
    ("shoe", "gun") : "SHOE WINS BECAUSE I SAID SO",
    ("gun", "cheeseburger") : "AMERICA #1 U S A U S A",
    ("knife", "toyota corolla") : "Knife is used to slash the corollas tires!",
    ("sock", "knife") : "Scariest sock puppet ever made",
    ("knife", "human") : "Is blood supposed to be inside or outside?",
    ("knife", "banana") : "Overkill but ok",
    ("airplane", "knife") : "...",
    ("bug", "knife") : "In a shocking twist the bug grabs the knife and goes straight for the throat",
    ("knife", "computer") : "asdyufisadijadsfoijjadsoifhasidjfnasd",
    ("knife", "fork") : "Who uses a knife on a banana? Do you think you are better than us?",
    ("knife", "the mediterranean sea") : "no dice",
    ("knife", "shoe") : "I dont have a quip for this one",
    ("knife", "cheeseburger") : "Sharing is caring",
    ("toyota corolla", "sock") : "Now i have a driving sock",
    ("toyota corolla", "human") : "Vehicular Manslaughter? Since when is it illegal for men to laugh your honor?",
    ("banana", "toyota corolla") : "The corolla mario carts off the highway",
    ("airplane", "toyota corolla") : "Plane runs over car (karma)",
    ("toyota corolla", "bug") : "Corolla runs over bug",
    ("computer", "toyota corolla") : "Computer ordered a drone strike on the corolla",
    ("fork", "toyota corolla") : "Tire goes usadfndjslakfsdfjsddasf",
    ("toyota corolla", "the mediterranean sea") : "PSA : Please throw your car batteries in the ocean, fish need to power their cars too",
    ("toyota corolla", "shoe") : "why?",
    ("toyota corolla", "cheeseburger") : "I dont get the hype fro five guys. Its fine I guess but nothing crazy special. Oh also corolla wins",
    ("human", "sock") : "Human is wearing crocks.",
    ("sock", "banana") : "??? I cant imagine what this is for",
    ("sock", "airplane") : "Did you know that more people die in sock related accidents, then car accidents?",
    ("sock", "bug") : "More people die wearing socks, than wearing bugs.",
    ("computer", "sock") : "Enjoy your programming socks",
    ("fork", "sock") : "Eat all of your sock before dessert",
    ("sock", "the mediterranean sea") : "It soaked it all up",
    ("sock", "shoe") : "A classic duo",
    ("sock", "cheeseburger") : "Burgerkeeng fut letuce",
    ("human", "banana") : "NO CAPTION FOUND",
    ("human", "airplane") : "Did you know that 100% of people who die in a plane crash have at some point in their lives been on a plane?",
    ("human", "bug") : "Let down and hanging around",
    ("computer", "human") : "The internet was a mistake",
    ("fork", "human") : "Cannibalism",
    ("human", "the mediterranean sea") : "He drank it all",
    ("shoe", "human") : "Human is too op.",
    ("human", "cheeseburger") : "American",
    ("banana", "airplane") : "Mario cart reference",
    ("banana", "bug") : "Cavendish worms",
    ("banana", "computer") : "bananacat.gif",
    ("fork", "banana") : "Sociopath behavior",
    ("banana", "the mediterranean sea") : "It was a very ver close fight",
    ("banana", "shoe") : "*Comically slips on bana peel",
    ("cheeseburger", "banana") : "Anyone who eats a banana cheeseburger should be drug out onto the street and shot",
    ("bug", "airplane") : "Bad time for the pilot to fins a wasp",
    ("computer", "airplane") : "Did nobody watch airplane 2?",
    ("fork", "airplane") : "MMMMMM iron",
    ("the mediterranean sea", "airplane") : "I imagine this has happened before",
    ("airplane", "shoe") : "WOW I WONDER WHO IS GONNA WIN",
    ("airplane", "cheeseburger") : "???????",
    ("bug", "computer") : "The computer science experience",
    ("bug", "fork") : "Git nightmare",
    ("bug", "the mediterranean sea") : "i am so done writing these things",
    ("shoe", "bug") : "An iconic duo",
    ("bug", "cheeseburger") : "Yummy",
    ("computer", "fork") : "You create a new branch from main",
    ("computer", "the mediterranean sea") : "Computer remotely launches a ballistic missile",
    ("shoe", "computer") : "Please i am so tired of writing these things free me",
    ("computer", "cheeseburger") : "HELP I WAS KIDNAPPED AND AM BEING FORCED TO WRITE THESE",
    ("fork", "the mediterranean sea") : "SOMEBODY SEND FOOD I HAVE NOT EATEN IN WEEKS",
    ("fork", "shoe") : "MMMMMMMMMMMMMMM delicious",
    ("fork", "cheeseburger") : "Psychopath behavior",
    ("the mediterranean sea", "shoe") : "trash belongs in the ocean",
    ("the mediterranean sea", "cheeseburger") : "Who lives in a pinnacle under the sea?",
    ("shoe", "cheeseburger") : "You think that will stop me from eating it?",
}

rps_track_wins : bool
rps_points : bool
rps_win_points : int

# ////////////////////////////////////////////////////////////////////////////////////

async def rock_paper_scissors(message : discord.Message):

    bot_choice : str = random.choice(possibilities)
    player_choice : str = ""

    for item in possibilities:
        if item in message.content:
            player_choice = item
            break

    text : str = "You chose : **" + player_choice.upper() + "**\n"
    text += "I chose : **" + bot_choice.upper() + "**\n\n"

    if bot_choice == 'thermonuclear ballistic missile':
        text += "You, and everything in a 10 mile radius dies\n"
        text += "# I WIN AHAHAHAHAHAHAHAHAHA"

    elif bot_choice == player_choice:
        text += "Great minds think alike\n# TIE"

    else:
        for combo in possible_games:
            if combo[0] == player_choice and combo[1] == bot_choice:
                text += "*" + possible_games.get(combo) + "*\n"
                text += player_choice + " beats " + bot_choice + "\n"
                text += "# YOU WIN"
                break
            elif combo[1] == player_choice and combo[0] == bot_choice:
                text += "*" + possible_games.get(combo) + "*\n"
                text += bot_choice + " beats " + player_choice + "\n"
                text += "# I WIN"
                break

    await message.reply(text)

"""
def print_combinations(choices_1, choices_2):
    for i, choice1 in enumerate(choices_1):
        for choice2 in choices_2[i+1:]:  
            print(f"(\"{choice1}\", \"{choice2}\") : \"\",")


choices = ['rock', 'paper', 'scissors', 'lizard', 'spock', 'mouse', 'worm', 'batman', 'snake', 'gun', 'knife', 'toyota corolla', 'sock', 'human', 'banana', 'airplane', 'bug', 'computer', 'fork', 'the mediterranean sea', 'shoe', 'cheeseburger']
print_combinations(choices, choices)
"""