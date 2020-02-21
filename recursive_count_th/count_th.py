'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Checking to see if the length of the word is less than 2, as "th" is two letters
    if len(word) < 2:
        return 0
    if word[0:2] == "th":
        # Moving through the string 2 letters ("th") at a time
        # If two letters side-by-side are "th", then the value increments by 1
        # This continues until hitting the end of the string
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
