import os
import random

import discord

# ////////////////////////////////////////////////////////////////////////////////////

# WHERE PROBLEM IMAGES LIVE
problems_folder : str = "./problems"

# TOPIC KEYWORDS -> PROBLEM SUBFOLDER NAME
problem_topics : dict = {
    ("linked list", "linked lists", "linkedlist", "linkedlists", "ll"): "Linked Lists",
    ("binary tree", "binary trees", "binary search tree", "binary search trees", "bst", "bsts"): "Binary Trees",
    ("avl tree", "avl trees", "avl"): "AVL Trees",
    ("hash table", "hash tables", "hashtable", "hashtables", "hash", "hashing"): "Hashing",
    ("heap", "heaps"): "Heaps",
    ("queue", "queues"): "Queues",
    ("stack", "stacks"): "Stacks",
    ("trie", "tries", "prefix tree", "prefix trees"): "Tries",
    ("recurrence relation", "recurrence relations", "recurrence"): "Recurrence Relations",
    ("recursion", "recursive"): "Recursion",
    ("dma", "dynamic memory allocation", "dynamic memory", "memory allocation"): "DMA",
    ("base conversion", "base conversions", "number system", "number systems"): "Base Conversion",
    ("algorithm analysis", "algo analysis", "big o", "big-o", "runtime", "run-time", "time complexity"): "AlgoAnal",
    ("bitwise", "bitwise operations", "bit manipulation", "bit operations", "bits"): "Bitwise",
    ("summation", "summations", "sum", "sums", "series"): "Summations",
    ("bubble sort", "insertion sort", "selection sort", "n squire sort", "n squire sorts", "n squared sorts",
     "n^2 sorts", "quadratic sort", "quadratic sorts", "merge sort", "mergesort", "quick sort", "quicksort",
     "quick select", "quickselect", "sort", "sorts", "sorting"): "Sorting",
}

# TOPICS THAT HAVE SLIDES BUT NO PRACTICE PROBLEMS -> SHOW THE SLIDES INSTEAD
no_problem_topics : tuple = (
    ("c review", "c-review"),
)

# ////////////////////////////////////////////////////////////////////////////////////

# FILES IN A PROBLEM SUBFOLDER
def problem_files(folder : str) -> list:
    path = os.path.join(problems_folder, folder)

    if not os.path.isdir(path):
        return []

    return sorted(
        os.path.join(path, name)
        for name in os.listdir(path)
        if os.path.isfile(os.path.join(path, name))
    )

# ////////////////////////////////////////////////////////////////////////////////////

# FOLDER FOR THE TOPIC MENTIONED (LONGEST KEYWORD WINS), OR NONE
def match_topic(content : str):
    folder = None
    length = 0

    for keywords, name in problem_topics.items():
        for keyword in keywords:
            if keyword in content and len(keyword) > length:
                folder = name
                length = len(keyword)

    return folder

# ////////////////////////////////////////////////////////////////////////////////////

# SEND A RANDOM PRACTICE PROBLEM
# RETURNS FALSE WHEN THERE ARE NO PROBLEMS SO THE SLIDES CAN BE SENT INSTEAD
async def practice_problem(message : discord.Message):
    folder = match_topic(message.content)

    # TOPIC FOUND
    if folder is not None:
        files = problem_files(folder)

        # TOPIC HAS NO PROBLEMS -> FALL THROUGH TO SLIDES
        if not files:
            return False

    # NO PROBLEM TOPIC -> TOPICS WITH ONLY SLIDES FALL THROUGH, ELSE RANDOM
    else:
        if any(keyword in message.content for keywords in no_problem_topics for keyword in keywords):
            return False

        folders = [
            name
            for name in os.listdir(problems_folder)
            if os.path.isdir(os.path.join(problems_folder, name)) and problem_files(name)
        ] if os.path.isdir(problems_folder) else []

        if not folders:
            return False

        files = problem_files(random.choice(folders))

    await message.channel.send(file=discord.File(random.choice(files)))
