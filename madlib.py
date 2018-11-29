"""Recreates the game of Mad Libs, prompting user for
parts of speech and combining them into a silly story.
"""

import re

regex = r"\{(.*?)\}"


def greeting():
    """Greet the user and provide instructions."""
    print("Let's write a silly story. I'm going to prompt you for some parts")
    print(" of speech and when I have everything I need, I'll tell you the")
    print("resulting story\n")


def read_file(path):
    """Read a file and return the data as a giant string."""
    with open(path, 'r') as rf:
        data = rf.read()
        return data


def parse_matches(data):
    """Use regex to find all parts of speech to modify."""
    matches = re.findall(regex, data)
    return matches


def change_matches(matches):
    """Ask the user for input to be inserted back into the story."""
    user_in = {}
    for item in matches:
        print('Please give me an', item.lower(), ': ', end='')
        new = input()
        user_in[item] = new
    return user_in


def reinsert_matches(user_in):
    """Recombines the matches into the story. Currently broken."""
    data = open('test.txt')
    for line in data:
        line.replace('{', '')
        line.replace('}', '')
    # to_change = re.findall(regex, data)
    # new = re.compile(r'[{}]', flags=re.UNICODE)
        print(line)


if __name__ == "__main__":
    greeting()
    story = read_file('test.txt')
    changes = parse_matches(story)
    madlibs = change_matches(changes)
    print(madlibs)
    reinsert_matches(madlibs)
