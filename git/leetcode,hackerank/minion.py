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

s = "BANANA"


def minion_game(s):
    # your code goes here
    vowels = "AEIOU"
    kevscr = 0
    stuscr = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevscr += len(s)-i
        else:
            stuscr += len(s)-i

    if kevscr > stuscr:
        print("Kevin", kevscr)
    elif stuscr > kevscr:
        print("Stuart", stuscr)
    elif kevscr == stuscr:
        print("Draw")


minion_game(s)
