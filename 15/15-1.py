

def get_input():
    with open("15.txt", "r") as f:
        return [i for i in f.read().split(",")]
    

def algo(string):
    val = 0
    for s in string:
        val += ord(s)
        val = val *17
        val = val % 256
    return val


def main():
    input = get_input()
    sum = 0
    for i in input:
        sum += algo(i)
    print(sum)

main()

# 510273