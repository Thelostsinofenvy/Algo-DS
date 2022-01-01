s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]
distance_apples = []
distance_oranges = []

# brute force


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0

    for i in apples:
        num1 = a + i
        distance_apples.append(num1)

    for i in oranges:
        num2 = b + i
        distance_oranges.append(num2)

    for apple in distance_apples:
        if apple >= s and apple <= t:
            count_apple = count_apple + 1

    for orange in distance_oranges:
        if orange >= s and orange <= t:
            count_orange += 1

    print(count_apple)
    print(count_orange)
