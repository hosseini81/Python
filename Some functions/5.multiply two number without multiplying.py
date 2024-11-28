


a, b = map(int, input('Type two number like "3 4": ').split())

def mult(a, b):
    if b == 1:
        return a
    return a + mult(a, b - 1)

print(f"{a} * {b} = {mult(a, b)}")