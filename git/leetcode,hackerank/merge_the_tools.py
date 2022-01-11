string = "AABCAAADA"
k = 3


def merge_the_tools(string, k):
    # divide string by k into equal parts.
    substr = []
    # n = int(len(string)/k) not this apparently
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        substr.append(sub)

    # remove duplicates from the substrings
    new_str = []
    for i in substr:
        for j in i:
            if j not in new_str:
                new_str.append(j)
        print("".join(new_str))
        new_str = []


merge_the_tools(string, k)
