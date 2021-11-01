array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
mylist = []
mydict = {}
# should return 2 as it is the first recurring character

# brute force
# On^2


def recurring(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return array[i]


# better solution


def alternative(array):
    for i in range(0, len(array)):
        if array[i] not in mylist:
            mylist.append(array[i])
    return mylist[0]


def usinghash(array):
    for i in range(0, len(array)):
        if array[i] in mydict:
            return array[i]
        else:
            mydict[array[i]] = i
    return mydict


print(usinghash(array))
