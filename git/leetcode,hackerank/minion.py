# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets + 1 point for each occurrence of the substring in the string .

# For Example:
# String = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

s = "BANANAeiou"


def minion_game(s):
    # your code goes here
    charlist = []
    for i in s:
        charlist.append(i.lower())
    print(charlist)

    vowels = []
    for vow in charlist:
        if vow == 'a' or vow == 'e' or vow == 'i' or vow == 'o' or vow == 'u':
            vowels.append(vow)
    non_duplicate = list(set(vowels))
    print(non_duplicate)


minion_game(s)
