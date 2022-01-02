print("Type 'encode' to encrypt , type decode to decrypt:")
ans = input()
print("type your message:")
s = input()
print("Type the shift number:")
shift = input()


def cipher():
    if ans.lower() == "encode":
        result = []
        for i in s:
            char = chr(ord(i) + int(shift))
            result.append(char)
        print(*(result))
    else:
        print("Please type encode or decode correctly!")


cipher()

print("type 'yes' if you want to go again. otherwise type 'no'")
repeat = input()
if repeat == 'yes':
    cipher()
else:
    print("see ya")
