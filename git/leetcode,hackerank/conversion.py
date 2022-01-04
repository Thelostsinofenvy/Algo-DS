def print_formatted(number):
    # your code goes here

    for i in range(1, +n+1):
        decimal = float(i)
        octal = oct(i)
        hed = hex(i)
        binary = bin(i)
        print(str(i) + " ", octal[2:] + " ", hed[2:].upper() + " ", binary[2:])


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
