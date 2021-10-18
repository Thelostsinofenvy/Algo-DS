arr = [1, 3, 5, 7, 9]

cur_sum = 0


def minmaxsum(arr):
    x = sum(arr)
    print(x-max(arr), (x-min(arr)))


minmaxsum(arr)
