"""Recreates the game of Mad Libs, prompting user for
parts of speech and combining them into a silly story.
"""

import re


def greeting():
    """Greet the user and provide instructions."""
    print("Let's write a silly story. I'm going to prompt you for some parts")
    print(" of speech and when I have everything I need, I'll tell you the")
    print("resulting story\n")


def read_file(path):
    """Read path and return the data as a giant string."""
    with open(path, 'r') as rf:
        return rf.read()


def write_file(path, out):
    """Write a file back to the given path."""
    with open(path, 'w') as wf:
        return wf.write(out)


def get_keys(format_string):
    """Get parts of speech to be modified."""
    key_list = []
    end = 0

    repetitions = format_string.count('{')
    for i in range(repetitions):
        start = format_string.find('{', end) + 1
        end = format_string.find('}', start)
        key = format_string[start:end]
        key_list.append(key)

    return key_list


def remove_keys(format_string):
    """Remove the parts of speech from the text for modification."""
    regex = r"\{.*?\}"
    output = re.sub(regex, '{}', format_string)
    return output


def parse(raw):
    """
    Parse input for further processing.

        get_keys is called to get the parts of speech to be modified
        remove_keys is called to strip the parts of speech to be replaced
    """
    prompts = get_keys(raw)
    stripped = remove_keys(raw)
    return prompts, stripped


def add_response(prompt, responses):
    if prompt[0] == 'A' or 'I':
        # In case the user is asked for an adjective or interjection
        # Can't help but fix grammar whenever possible
        response = input(f'Enter an {prompt}: ')
        responses.append(response)
    else:
        response = input(f'Enter a {prompt}: ')


def get_responses(prompts):
    responses = []

    for prompt in prompts:
        add_response(prompt, responses)

    return responses

def output_story(raw):
    prompts, stripped = parse(raw)
    responses = get_responses(prompts)
    story = stripped.format(*responses)
    return story


if __name__ == "__main__":
    greeting()
    raw = read_file('test.txt')
    story = output_story(raw)
    write_file('madlib_complete.txt', story)
