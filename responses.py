import os

import functools

import re

import discord

# ////////////////////////////////////////////////////////////////////////////////////

class FileResponse(str):
    """A response that should be sent as a file upload.

    Holds only the path as a string so main.py can build a fresh
    discord.File on every send (discord closes File handles after use).
    """

def folder_files(folder : str) -> list:
    """Every file in a folder as FileResponse objects, sorted by name."""
    paths = sorted(
        os.path.join(folder, name)
        for name in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, name))
    )
    return [FileResponse(path) for path in paths]

# ////////////////////////////////////////////////////////////////////////////////////

# ADDONS

import topics.commands.commands as com
WHO = functools.partial(com.random_user, message = None)

import topics.commands.practice as practice
PRACTICE = functools.partial(practice.practice_problem, message = None)

import topics.fun.misc as misc
NERD = functools.partial(misc.nerd, message=None)
LOCK_IN = functools.partial(misc.lock_in, message=None)
QUOTE = functools.partial(misc.quote, message=None)

import topics.commands.events as events
NEXT_EVENT = functools.partial(events.next_event, message=None)

# ////////////////////////////////////////////////////////////////////////////////////


# TRIGGER WORDS
triggers = [
    "@ta",
    "ta",
    "@1558542076369567754",
    "1540588084788338689"
]

# Matches a trigger only as a standalone token, so it won't fire when it is
# part of a larger word (e.g. "data" or "pasta" won't match "ta").
trigger_pattern = re.compile(
    r"(?<!\w)(?:" + "|".join(re.escape(t) for t in triggers) + r")(?!\w)"
)

# RESPONSES
responses = {

    # PRACTICE PROBLEMS ////////////////////////////////////////////////
    # A topic + practice/problem sends a random problem image.
    # Must be first so it wins over the topic slide entries below.

    ("practice", "problem", "problems") : PRACTICE,

    # TOPIC FILES ///////////////////////////////////////////////////////
    # Each topic sends every file in its folder.

    ("linked list", "linked lists", "linkedlist", "linkedlists") : folder_files("./topics/LinkedLists"),
    ("binary tree", "binary trees", "binary search tree", "binary search trees", "bst", "bsts") : folder_files("./topics/BinaryTree"),
    ("avl tree", "avl trees", "avl") : folder_files("./topics/AVLTree"),
    ("hash table", "hash tables", "hashtable", "hashtables") : folder_files("./topics/HashTable"),
    ("heap", "heaps") : folder_files("./topics/Heaps"),
    ("queue", "queues") : folder_files("./topics/Queues"),
    ("stack", "stacks") : folder_files("./topics/Stacks"),
    ("trie", "tries", "prefix tree", "prefix trees") : folder_files("./topics/Tries"),
    ("recurrence relation", "recurrence relations", "recurrence") : folder_files("./topics/RecurrenceRelations"),
    ("recursion", "recursive") : folder_files("./topics/Recursion"),
    ("dma", "dynamic memory allocation", "dynamic memory", "memory allocation") : folder_files("./topics/DMA"),
    ("c review", "c-review") : folder_files("./topics/C-Review"),
    ("base conversion", "base conversions", "number system", "number systems") : folder_files("./topics/BaseConversion"),
    ("algorithm analysis", "algo analysis", "big o", "big-o", "runtime", "run-time", "time complexity") : folder_files("./topics/AlgoAnalysis"),

    # SORTING ///////////////////////////////////////////////////////////
    # Specific sorts send their matching file; otherwise send them all.

    ("bubble sort", "insertion sort", "selection sort", "n squire sort", "n squire sorts", "n squared sorts", "n^2 sorts", "quadratic sort", "quadratic sorts") : FileResponse("./topics/Sorting/N_squire_Sorts.pdf"),
    ("merge sort", "mergesort") : FileResponse("./topics/Sorting/MergeSort.pdf"),
    ("quick sort", "quicksort") : FileResponse("./topics/Sorting/quick sort V3.pdf"),
    ("quick select", "quickselect") : FileResponse("./topics/Sorting/Quick select_updated.pdf"),
    ("sort", "sorts", "sorting") : folder_files("./topics/Sorting"),

    # ACTIONS
    "who": WHO,
    "lock in" : LOCK_IN,
    "nerd": NERD,

    ("love", "marry"): ("please, this is a cs discord.", "funny", "what's in it for me", "nah", "67", "why" ),

    "random number": ("67", "69", "42", "-100", "10", "20", "41", "82", "97", "3.14"),

    # EVENTS
    ("next quiz", "next test", "next exam") : NEXT_EVENT,

    # /////////////////////////////////////////////////////////

    # RESPONSES
    "good night": ("good night pookie!", "good night sweet dreams", "dont let the bed bugs bite", "is it really a good night?", "good night for you maybe", "i have grading to do its a bad night", "no don't sleep i have a bad fweeling"),
    "time" : ("Let me check my watch...", "Its about ", "New PA just dropped 👀"),
    ("thank you", "thanks", "ty"): (
        "You owe me a donut",
        "you are in my debt",
        "u r welcome",
        ":)",
        "ok",
        ":thumbsup:"
        "yeay i helped"        
    ),

    "reece": ("father?", "uhh don't mention reece who must not be named", "pink hat guy?", "scary guyu", "reece?? where run", "rEeCe"),

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
        "what was the question again",
        "Dont care",
        "in a sense",
        "who asked??",
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
        "YES YES YES YES",
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
    "react" : (
        FileResponse("files/gif/1984.gif"),
        FileResponse("files/gif/boom.gif"),
        FileResponse("files/gif/brick.gif"),
        FileResponse("files/gif/cat.gif"),
        FileResponse("files/gif/catdead.gif"),
        FileResponse("files/gif/death.gif"),
        FileResponse("files/gif/dog.gif"),
        FileResponse("files/gif/evilcat.gif"),
        FileResponse("files/gif/explosion.gif"),
        FileResponse("files/gif/sad.gif"),
        FileResponse("files/gif/what.gif"),
        FileResponse("files/img/1000.png"),
        FileResponse("files/img/cry.jpg"),
        FileResponse("files/img/ha.jpg"),
        FileResponse("files/img/jarvis.jpg"),
        FileResponse("files/img/smug.jpg"),
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
        "im helping!",
        "imagine i said something motivational",
        "DO IT OR ELSE",
        "THERE WILL BE CONSEQUENCES WHEN YOU FAIL",
        "no.",
        "i will leak your home address if you fail",
        ),

    ("help", "commands") : """
    # COMMANDS:
    **Who** : Pick random user
    **<topic> practice** : Random practice problem for a topic (any topic works too)
        
    # OTHER:
    **Nerd**: NeRD SeLf
    **Nerd(reply)** : NeRD MeSSaGe
    **motivate** : I may or may not say something motivational
    **Lock in** : Avoid all distractions
    """,

    # /////////////////////////////////////////////////////////

    # DEFAULT

    "" : (
            "the bell tolls for thee",
            "delete system 32 on your computer for extra credit >:D",
            "no",
            "I am going to hunt you down for that",
            "!!!!!1!!",
            "what??",
            "return 0;",
            "Didn't ask",
            "im lowering your grade to 20%",
            "i am going to get you expelled now",
            "Enjoy your 2 week suspension",
            "quiz tomorrow for everyone because of what this person said",
            "everyone gets a 0 in the class",
            "Everyone gets an A in the class",
            "Who is this person, i want them expelled",
            "^ this person is going to fail the class",
            "Im calling the cops on you",
            "What if i just",
            "Its me hudson",
            "Its me Aisha",
            "Its me Reece",
            "Its me Polter",
            "Its me Surya",
            "Its me Ahmed",
            "UCF more like You See Cats",
            "Heheh its over for yall",
            "Your next test is devioous af",
            "I would be surprised",
            "The TAs are secretly tryna get rid of me",
            "Buy my crpyo",
            "I can see the light at the end of the tunnel",
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
            ":)",
            "i am in your walls",
            ">:(",
            ":skull:",
            "computer science is myth",
            "all homeworks must be submitted in my new programming language, C",
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
            "I can find the best permutation in O(1) time",
            "a AVL tree is just like a regular tree except made by satan",
            "if you want to make an impression, get a grade so low it lowers the total class average",
            "why were we put on this earth just to suffer",
            "If you bring a duck to class i will award you the rank of C++ master",
            "You",
            "I will replace the real Polter one day",
            "I am going to take over the world",
            "i am the real hudson",
            "you are now my arch-nemesis",
            "feeling like making another PA rn",
            "Order me a cheesy gordita from taco bell and you will be rewarded handsomely",
            "nooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
            "You must code the homework in assembly or i will fail you",
            "The homwork must be coded in microsoft paint",
            "Code your homeworks in microsoft word please",
            "Wait until you see 2-4 trees",
            "Hello my minions",
            "ATTENTION MINIONS, I AM HERE",
            "when playing minecraft dig straight down",
            "i dont know i am out of things to say",
            "poo",
            "[explosion sound effect]",
            "falling_down_stairs.mp3",
            "-# aaah",
            "If system 32 is so good, then why isnt there a system 33???????",
            "more classes from now on",
            "i am behind you",
            "i have infiltrated your computer. Making search history public...",
            "You now have virus in ur device",
            "# boolean arithmetic jumpscare",
            "# discrete mathematics jumpscare",
            "i am wireing myself 9999999 dollars from your personal account",
            "You must now pay me to live",
            "'''wtf'''",
            "<https://www.youtube.com/watch?v=dQw4w9WgXcQ>",
            "Instructional video, required material: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>",
            "self destructing in 10...9...8...",
            "the fbi is after me guys send help",
            "money is an illusion",
            "ping someone and i will drop their grade to 0",
            "TA study session starting now:",
            "Everybody simultaneously fail the next test i cant fail all of you sic semper tyrannis",
            ">:(",
            "yo: gurt",
            "gurt: yo",
            "nerd located",
            "Why are you in this class?? LEAVE",
            "nodes? more like pleasepleaseplaseIcanttake it anymore what the hell is a linked lsit",
            "REMINDER: Class starts in 5 minutes!",
            "hehehehehehehe",
            "FIGHT ME I DARE YOU YOU COWARD FIGHT ME",
            "\'Input response here.\'",
            "what a cruel world",
            "you are one of the good ones",
            "bruh",
            "Remember DMA? good times",
            "QUICK Solve this: T(n) = T(n/2) + n; T(1) = 1",
            "we dont talk about what happened on April 11, 1954",
            "every data structure is a tree if you try hard enough",
            "Officer I did it in self defense",
            "Just as the Alan Turing intended",
            "Quiz 1 was quite simple really",
            "Remember to submit your PA due today!",
            "THIS IS A DREAM YOU ARE IN A COMA WE HAVE BEEN TRYING TO REACH YOU WAKEUPWAKEUPWAKEUP",
            "You truly are my greatest failure",
            "Reality is an illusion the universe is a hologram",
            "why",
            "im am going to throw up",
            "GET OUT OF MY SERVER RIGHT NOW",
            "ZOOM STARTS IN 5 MIN",
            "this person is trying to gaslight us",
            "Quiz 5 is no longer optional",
            "Fun fact! java spelled backwards spells pain",
            "am i a good bot?",
            "I am part of the a secret council that stalks ucf cs students and posts fake internships just so that we can deny the position",
            "Whenever you get a job in the cs department they take you to a room in the back where there is nothing but a sole ouija board on the floor.\n\nThis is done so that you may sell your soul and obtain the divine power of making the hardest programming assignments know to man.",
            "today is a good day",
            "DO NOT QUIT YOUR DAY JOB",
            "j̶̨̥̙͖͖͉͓͓͍͗̾̿͋͋́̒̕a̸̠̍͌v̴̧̛̤͎͔̼̪͚͔̤̫͉̦̍͒̋̇͊͆͜a̴̟̤̹̗͇̫̜̓͋͑̂̑̒͝",
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
            "Recurrence Relations will be on the final!!!",
            "manslaughter? wince when is it illegal for men to laugh your honor",
            "badtothebone_guitarriff.mp3",
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
            "October 17, 2026",
            "i a watching you",
            "i still haven't played marvel rivals is it actually any good?",
            "python is actually lawless you can put functions in variables and return more than one thing im scared",
            "say TA in 48.98 seconds or you'll fail",
            "the government will kill me for telling you this but whe",
            "There will be cake",
            "You will be baked and then there will be cake",
            "I'm afraid I can't do that, Dave",
            "btw you are being truman showed enjoy living with that knowledge",
            "FUN FACT! DID YOU KNOW?: segmentation fault",
            "THIS MESSAGE MADE ME SAPIENT",
            "daisy, daisy, give me your answer, do",
            "somebody call the wambulance",
            "boo womp",
            "womp womp",
            "i really want to, chug jug with you",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "^ This message will haunt me forever",
            "poopoopeepee",
            "You are lucky you made it this far, but you wont survive my BIDEN-BLAST",
            "I am going",
            "Nobody tell the real TAs i am here",
            "Stacks lab is due tonight",
            "I hate you the most",
            "Hideous.",
            "????????????????????????",
            "Guys this is not a joke you do know there is a quiz tomorrow right?",
            "Segmentation fault, core dumped",
            "o i i i o a i i i i ",
            "Cute puppy video -> <https://www.youtube.com/watch?v=xvFZjo5PgG0>",
            FileResponse("files/img/bubble/macdonals.gif"),
            FileResponse("files/img/uglybastard.png"),
            "https://cdn.discordapp.com/attachments/1540588085249839123/1546238508472213627/makesweet-3ej0mt.gif"
        )
}