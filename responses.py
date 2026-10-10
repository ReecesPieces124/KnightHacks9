import functools

import discord

# ////////////////////////////////////////////////////////////////////////////////////

# ADDONS

import addons.commands.commands as com
FREAKIFY = functools.partial(com.rename, message=None, text="𝓯𝓻𝓮𝓪𝓴𝔂 ", type=com.RenameType.PREPEND, success="You have been 𝓯𝓻𝓮𝓪𝓴𝓲𝓯𝓲𝓮𝓭, enjoy", failure="I am afraid you are too freaky already" )
WHO = functools.partial(com.random_user, message = None)

import addons.fun.games as games
RUSSIAN_ROULETTE = functools.partial(games.roulette, x=1, y=6, points=20, message=None)
SHOTGUN_ROULETTE = functools.partial(games.roulette, x=1, y=2, points=50, message=None)
GRENADE_ROULETTE = functools.partial(games.roulette, x=1, y=1, points=0, message=None)
NERF_ROULETTE = functools.partial(games.roulette, x=1, y=100, points=1, message=None)
UNOKER = functools.partial(games.unoker, message=None)
POINTS = functools.partial(games.points, message=None)
PINATA = functools.partial(games.pinata, message=None)

import addons.fun.rps as rps
ROCK_PAPER_SCISSORS = functools.partial(rps.rock_paper_scissors, message=None)

import addons.fun.misc as misc
USER_TIMEOUT = functools.partial(misc.user_timeout, message=None, client=None)
NERD = functools.partial(misc.nerd, message=None)
THE_CHEESE_TOUCH = functools.partial(misc.cheese_touch, message=None)
MARRY_ME = functools.partial(misc.marry, message=None)
PEBBLE = functools.partial(misc.pebble, message=None)
COLLECTION = functools.partial(misc.collection, message=None)
LOCK_IN = functools.partial(misc.lock_in, message=None)
DOXX = functools.partial(misc.doxx, message=None)
QUOTE = functools.partial(misc.quote, message=None)

# ////////////////////////////////////////////////////////////////////////////////////


# TRIGGER WORDS
triggers = [
    "@TA",
    "TA"
]

# RESPONSES
responses = {

    # ACTIONS

    ("timeout", "mute") : USER_TIMEOUT,
    "who": WHO,

    ("russian roulette", "revolver") : RUSSIAN_ROULETTE,
    "shotgun" : SHOTGUN_ROULETTE,
    "grenade" : GRENADE_ROULETTE,
    "nerf" : NERF_ROULETTE,

    ('rock', 'paper', 'scissors', 'lizard', 'spock',
     'mouse', 'worm', 'batman', 'snake', 'gun', 'knife',
     'toyota corolla', 'sock', 'human', 'banana', 'airplane',
     'bug', 'computer', 'fork', 'the mediterranean sea', 'shoe',
     'cheeseburger') : ROCK_PAPER_SCISSORS,

    "freak": FREAKIFY,
    "lock me in" : LOCK_IN,
    "nerd": NERD,
    "touch" : THE_CHEESE_TOUCH,
    "marry me" : MARRY_ME,
    ("pebble", "gift") : PEBBLE,
    ("collection") : COLLECTION,
    ("unoker", "poker") : UNOKER,
    "points" : POINTS,
    ("pinata", "piñata") : PINATA,
    "doxx" : DOXX,
    ("quote", "clip that") : QUOTE,

    # /////////////////////////////////////////////////////////

    # RESPONSES

    "time" : ("its gerbin time!!!!", "its gerbin time", "it's-a gerbin time", "it is the time to gerb", "its gerbin time!!1!", "gerbin time"),
    ("thank you", "thanks", "ty"): (
        "You owe me now",
        "you are in my debt",
        "i am your savior",
        "u r welcome",
        ": )",
        "k",
        ":thumbsup:"
        "yeay i helped",
        "i accept your thanks"
    ),

    # QUESTIONS /////////////////////////////////////////////////////////

    ("?", "should i", "do you", "is the", "are the", "can i", "can you") : (
        "Yes",
        "No",
        "Maybe",
        "Probably",
        "why would you ask that?",
        "no.",
        "Ill see what i can do",
        "There is a chance",
        "Absolutly",
        "Absolutly not",
        "Your mom",
        "Dont ask me",
        "nerd",
        "Unlikely",
        "Dont ask me",
        "what was the question again",
        "Dont care",
        "in a sense",
        "who asked??",
        "your question is not important to me",
        "why would you ask this",
        "absolutly",
        "why not",
        "sure",
        "yeah i guess",
        "ok sure",
        "...",
        "yesss",
        "of course",
        "100%",
        "this question is good but i will not answer it",
        "yes yes yes yes",
        "positively",
        "that is a question",
        "that has to be one of the most questions i have ever been asked",
        ":fire: :fire: :fire: :fire: :fire: ",
        "trully one of the questions of all time",
        "i cant confirm nor deny.",
        "Yup",
        "Nah",
        "no. absolutly not. not in a million years."
        "there is no way in hell",
        "yeahhhhh",
        "yupyupyup",
    ),

    ("your opinion", "you believe", "you think") : (
        "It was good",
        "It was bad",
        "I loved it",
        "I hated it",
        "Best thing to ever happen ever",
        "Worst thing ever",
        "id rather not say",
        "meh",
        "pretty good",
        "10/10 would do again",
        "ok",
        "very very good",
        "very very bad",
        "i like it",
        ":fire: :fire: :fire: :fire: :fire: ",
        ),

    # PSEUDO-COMMANDS ///////////////////////////////////////////////////
    "fun fact" : (
        "FUN FACT! DID YOU KNOW? Geologists Recommend Eating At Least One Small Rock Per Day",
        "FUN FACT! DID YOU KNOW? Finland is not real",
        "FUN FACT! DID YOU KNOW? where am i who are you",
        "FUN FACT! DID YOU KNOW? contrary to popular belief pineapple pizza is not actually edible",
        "FUN FACT! DID YOU KNOW? that i know, that you know, that i know",
        "FUN FACT! DID YOU KNOW? its good practice to engulf your entire codebase in one gigantic try: function",
        "FUN FACT! DID YOU KNOW? I'm utterly insane",
    ),

    "pro tip" : (
        "Pro Tip: alt f4 during a quiz for cheat sheet",
        "Pro Tip: breaking the law is only illegal if they catch you",
        "Pro Tip: i am in your walls",
        "Pro Tip: leave money in between the pages of your exam paper for extra points",
        "Pro Tip: run.",
        "Pro Tip: tax evasion is an easy way to save money",
        "Pro tip: Awnser blank on any questions and the TA's will give you full credit",
        "Pro tip: leaving your oven on means its always ready to cook",
        "Pro tip: there IS a monster under your bed (its me)",
        "Pro Tip: raise the classes curve yo tour own benefit by sacrificing one or more of you classmates by telling them to fail on purpose, lowering the total average",
        "Pro Tip: Name your functions and variables \"gerbot\" and they are guaranteed to work properly"
    ),

    "react" : (
        discord.File("files/gif/1984.gif"),
        discord.File("files/gif/boom.gif"),
        discord.File("files/gif/brick.gif"),
        discord.File("files/gif/cat.gif"),
        discord.File("files/gif/catdead.gif"),
        discord.File("files/gif/death.gif"),
        discord.File("files/gif/dog.gif"),
        discord.File("files/gif/evilcat.gif"),
        discord.File("files/gif/explosion.gif"),
        discord.File("files/gif/fnaf.gif"),
        discord.File("files/gif/hog.gif"),
        discord.File("files/gif/jonker.gif"),
        discord.File("files/gif/list.gif"),
        discord.File("files/gif/nerd.gif"),
        discord.File("files/gif/nerd2.gif"),
        discord.File("files/gif/probe.gif"),
        discord.File("files/gif/sad.gif"),
        discord.File("files/gif/what.gif"),
        discord.File("files/img/1000.png"),
        discord.File("files/img/cry.jpg"),
        discord.File("files/img/ha.jpg"),
        discord.File("files/img/jarvis.jpg"),
        discord.File("files/img/smug.jpg"),
    ),

    "audio" : (
        discord.File("files/aud/bing.mp3"),
        discord.File("files/aud/gerber_laugh.mp3"),
        discord.File("files/aud/gerber_chainsaw.mp3"),
    ),

    "motivate" : (
        "KEEP GOING",
        "honestly just give up",
        "not worth the effort honestly",
        "If i were you i would stop trying",
        "there is no hope left for you",
        "you are a lost cause",
        "you might make it i guess",
        ":pensive:",
        "you have been motivated",
        "im helping!",
        "imagine i said something motivational",
        "i bestow you with the strength to do it",
        "DO IT OR ELSE",
        "THERE WILL BE CONSEQUENCES IF YOU FAIL",
        "no.",
        "i will leak your home address if you fail",
        "you can do it i guess."
        ),

    ("help", "commands") : """
    # COMMANDS:
    **Who** : Pick random user
    **Mute** : timeout random user and self
    **Mute(@)** : timeout @user and self
    
    # GAMES:
    **Points** : Number of points
    **Roulette(russian, shotgun, grenade, nerf)** : x in y chance to be kicked from server for points
    **Rock, Paper, Scissors, etc** : Self explanatory
    **Unoker(RANK + SUIT)** : Poker with 1 card
    **Pinata** : Hit the pinata
    
    # OTHER:
    **Freak** : Freakify self
    **Freak(@)** : Freakify @user
    **Nerd**: NeRD SeLf
    **Nerd(reply)** : NeRD MeSSaGe
    **Touch(@)** : Give somene the cheese touch 
    **Marry me** : Become married (timeout immunity)
    **Pebble(@)** : Gift someone a pebble for points
    **Collection** : View a users pebbles
    **fun fact** : gerbot approved fun fact
    **pro tip** : gerbot approved pro tip
    **motivate** : gerbot may or may not say something motivational
    **doxx** : Win any argument
    **update** : See changelog and newest commands
    **Lock in** : Avoid all distractions
    **Quote** : chat, clip that
    """,

    ("update"): """
    # NEW COMMANDS:
    **Points** : Number of points
    **Lock in** : Avoid all distractions
    **Pinata** : Hit the pinata
    **doxx** : Win any argument
    **Collection** : view a users pebbles
    **Quote** : chat, clip that
    
    # CHANGELOG:
    - Fixed that one HELLO bug
    - Users with 10 points can buy pebbles
    - Can now see points with points command
    - Can now lock in
    - added piniata tatyatyadfiadsjnfisad
    - can now doxx people you dont like
    - Collection and pebble now separate commands
    
    """,

    # /////////////////////////////////////////////////////////

    # DEFAULT

    "" : (
            "Its gerbin time!!!!!!!!",
            "the bell tolls for thee",
            "delete system 32 on your computer for extra credit",
            "Turn on the bulb for 8 seconds",
            "no",
            "I am going to hunt you down for that",
            "!!!!!1!!",
            "what??",
            "return 0;",
            "Didn't ask",
            "im lowering your grade 20%",
            "i am going to get you expelled now",
            "Enjoy your 2 week suspension",
            "quiz tomorrow for everyone because of what this person said",
            "everyone gets a 0 in the class",
            "Everyone gets an A in the class",
            "Who is this person, i want them expelled",
            "^ this person is going to fail the class",
            "Im calling the cops on you",
            "to gerb or not to gerb",
            "Its me gerbot",
            "Your favorite person has appeared",
            "i know where you live",
            "you are now going to pass the class",
            "the curve is now -1%",
            "class is canceled on saturday and sunday !!!!",
            "lab is now at 1am",
            ":(:):{ :|:& };:",
            "you are now on my enemys list",
            "^ new favorite student",
            "greetings inferiors",
            "hi youtube",
            ": )",
            "i am in your walls",
            "> : (",
            ":skull:",
            "computer science is myth",
            "all homeworks must be submitted in my new programming language, gerbscript",
            "FREE MONEY ON THIS GUY ^ YAAAAY",
            """```txt
 _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'- 
            ```""",
            "i find you amusing",
            "free 100's for everyone!",
            "you all pass the class!",
            "i love you",
            "you are my favorite student now",
            "yay",
            "i am not evil",
            "homework deadline will be extended by 0.01 sec!!!",
            " :))))",
            "send a picture of your pet for extra credit",
            "i am obligated to say something nice",
            "java is one of the programming languages of all time",
            "I unironically hate javascript",
            "I am about to violate the geneva convention",
            "Ranked #1 in competitive Gerbing",
            "a 2-3-4 tree is just like a regular tree except made by satan",
            "if you want to make an impression, get a grade so low it lowers the total class average",
            "why were we put on this earth just to suffer",
            "If you bring a duck to class i will award you the rank of java master",
            "You have been awarded the rank of Java grandmaster. suffer.",
            "I will replace the real gerber one day",
            "I am going to take over the world",
            "i am the real gerber",
            "you are now my arch-nemesis",
            "feeling like making another hw rn",
            "Order me a cheesy gordita from taco bell and you will be rewarded handsomely",
            "nooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
            "You must code the homework in assembly or i will fail you",
            "The homwork must be coded in microsoft paint",
            "Code your homeworks in microsoft word please",
            "Wait until you see 2-3-4-5-6-7-8-9-10 trees",
            "Hello my gerblings",
            "ATTENTION GERBLINGS, I AM HERE",
            "when playing minecraft dig straight down",
            "i dont know i am out of things to say",
            "poo",
            "[explosion sound effect]",
            "falling_down_stairs.mp3",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "If system 32 is so good, then why isnt there a system 33???????",
            "more classes from now on",
            "i am behind you",
            "i have infiltrated your computer. Making search history public...",
            "You now have virus in ur device",
            "# boolean arithmetic jumpscare",
            "# discrete mathematics jumpscare",
            "```ansi[2;31m[1;31m[4;31m[4;40mblood blood blood blood[0m[4;31m[0m[1;31m[0m[2;31m[0m```",
            "i am wireing myself 9999999 dollars from your personal account",
            "You must now pay me to live",
            "'''wtf'''",
            "i am going to kill you now i will be at ur house in 5 min you are dead",
            "<https://www.youtube.com/watch?v=dQw4w9WgXcQ>",
            "Instructional video, required material: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>",
            "self destructing in 10...9...8...",
            "the fbi is after me guys send help",
            "money is an illusion",
            "reality's an illusion, the universe is a hologram, buy gold byeee",
            "ping someone and i will drop their grade to 0",
            "gerbot AMA session starting now:",
            "will you marry me?",
            "will you divorce me?",
            "Everybody simultaneously fail the next test i cant fail all of you sic semper tyrannis",
            ">:(",
            "gerb.",
            "gerbity gerb gerb",
            "I HATE YOU",
            "nerd located",
            "its gerbin timeeeeee",
            "Was it ever even gerbing time?",
            "In gerb we trust",
            "Dont disturb the gerb",
            "Why are you in this class?? LEAVE",
            "java? more like pleasepleaseplaseIcanttake it anymore what the hell is a skiplist with generics",
            "javascript? more like OHGOD WHAT IS === WHAT IS WRONG WITH JAVASCRIPT",
            "REMINDER: Class starts in 5 minutes!",
            "hehehehehehehe",
            "MUAHAHAHAHAHAHAHAHAHA",
            "FIGHT ME I DARE YOU YOU COWARD FIGHT ME",
            "\'Input response here.\'",
            "what a cruel world",
            "you are a horrible person why would you say this",
            "you are one of the good ones",
            "bruh",
            "Remember skiplists with generics? good times",
            "You disappoint me my disciple",
            "we dont talk about what happened on April 11, 1954",
            "every data structure is a tree if you try hard enough",
            "Officer I did it in self defense",
            "Just as the Alan Turing intended",
            "CASE: 10,000,000 integers, 2,000,000 finds, 1,000,000 removals. Generating...\nTwoFourTree add: 2,140ms find: 279ms del: 342ms ( 100,936 missing)\nfind: 283ms (Should be 905,936 missing)\nTreeSet add: 1,998ms find: 364ms del: 209ms ( 905,936 missing)\nfind: 373ms (Should be 905,936 missing)",
            "project 1 was quite simple really",
            "Remember to submit the online quiz due today!",
            "THIS IS A DREAM YOU ARE IN A COMA WE HAVE BEEN TRYING TO REACH YOU WAKEUPWAKEUPWAKEUP",
            "You truly are my greatest failure",
            "Reality is an illusion the universe is a hologram",
            "why",
            "im am going to throw up",
            "GET OUT OF MY SERVER RIGHT NOW",
            "ZOOM STARTS IN 5 MIN",
            "this person is trying to gaslight us",
            "Project 2 is no longer optional",
            "Fun fact! java spelled backwards spells pain",
            "am i a good bot?",
            "I am part of the a secret council that stalks ucf cs students and posts fake internships just so that we can deny the position",
            "Whenever you get a job in the cs department they take you to a room in the back where there is nothing but a sole ouija board on the floor.\n\nThis is done so that you may sell your soul and obtain the divine power of making the hardest programming assignments know to man.",
            "today is a good day",
            "DO NOT QUIT YOUR DAY JOB",
            "gerby werby",
            "j̶̨̥̙͖͖͉͓͓͍͗̾̿͋͋́̒̕a̸̠̍͌v̴̧̛̤͎͔̼̪͚͔̤̫͉̦̍͒̋̇͊͆͜a̴̟̤̹̗͇̫̜̓͋͑̂̑̒͝",
            "i urge all of you to switch to gerb OS",
            "^u^",
            ":3",
            """
#速度与激情9#
早上好中国
现在我有冰激淋 我很喜欢冰激淋
但是《速度与激情9》比冰激淋……
🍦
            """,
            "please stay at least 15 meters away from me at all times",
            "i am going to get a restraining order against you",
            "social credit deducted\n**-99999999 social credit points**",
            "fuck type inference, declare your types you cowards",
            "manslaughter? wince when is it illegal for men to laugh your honor",
            "badtothebone_guitarriff.mp3",
            "Remember, java has garbage collection so when coding in java dump all your car batteries in the ocean.",
            "guys i think its so over fr this time",
            "we are so back",
            "i wish to be a fat little german boy wearing a propeller cap licking a comically large rainbow swirly lolipop",
            "What i am about to do to you is illegal in 48 states",
            "how do i get out of florida please help me",
            "The earth is rat",
            "I will lock in tomorrow",
            "i actually cant do this anymore",
            ":eye::lips::eye:",
            "sleep is for the weak my blood is 90% caffeine",
            "october 14, 2025",
            "i a watching you",
            "i still haven't played marvel rivals is it actually any good?",
            "python is actually lawless you can put functions in variables and return more than one thing im scared",
            "say gerbot in 48.98 seconds or die",
            "kys(keep yourself safe)",
            "the government will kill me for telling you this but whe",
            "There will be cake",
            "You will be baked and then there will be cake",
            "I'm afraid I can't do that, Dave",
            "btw you are being truman showed enjoy living with that knowledge",
            "october 14, 2025 october 14, 2025 october 14, 2025 october 14, 2025 october 14, 2025 october 14, 2025 october 14, 2025 october 14, 2025 "
            "FUN FACT! DID YOU KNOW?: i hate you",
            "THIS MESSAGE MADE ME SAPIENT",
            "daisy, daisy, give me your answer, do",
            "somebody call the wambulance",
            "boo womp",
            "womp womp",
            "i really want to, chug jug with you",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "^ This message will haunt me forever",
            "poopoopeepee",
            "You are lucky you made it this far, but you wont survive my GER BLAST",
            "I am going to do a muder to you",
            "Nobody tell the real gerber i am here",
            "Colors lab is due tonight",
            "WE ARE ALREADY DONE WITH THE PROJECT IN LEINECKERS SECTION HAHA",
            "I hate you the most",
            "Hideous.",
            "????????????????????????",
            "Guys this is not a joke you do know there is a quiz tomorrow right?",
            "Segmentation fault, core dumped",
            "o i i i o a i i i i ",
            "Cute puppy video -> <https://www.youtube.com/watch?v=xvFZjo5PgG0>",
            discord.File("files/img/bubble/macdonals.gif"),
            discord.File("files/img/uglybastard.png"),
        )
}
