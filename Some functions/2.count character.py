string = input("Type your text: ")
char = input("Type that character you want to count: ")

def count_char(string, char):
    n = 0
    for i in range(len(string)):
        if string[i] == char:
            n += 1
    return n

print(count_char(string, char))