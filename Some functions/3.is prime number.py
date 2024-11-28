n = int(input("Type your number: "))

def is_prime(n):
    if n <= 1:
        return "No"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "No"
    return "Yes"

print(is_prime(n))