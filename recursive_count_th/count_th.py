'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    th_words = word.find("th")

    if th_words == 0:
        print("No occurences found.")
        return 0
    if th_words >= 1:
        print("Occurences were found")
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
