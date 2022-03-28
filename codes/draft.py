number = input("dsd")

def num_s(num):
    d = []
    for i in tuple(num):
        d.append(str((int(i) + 5)%10))
    d.reverse()
    return int("".join(d))

print(num_s(number))