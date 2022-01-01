if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

# converting tuple to hash (hackerank)

t = tuple(integer_list)


def hasher(t):
    return hash(t)


print(hasher(t))
