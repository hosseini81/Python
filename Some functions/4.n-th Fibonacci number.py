n =  int(input("n-th? "))

def fibonacci(n):
    if n <= 0: 
        return "Wrong input"
    if n == 1:
        return 0
    if n == 2:
       return 1
    if n > 2:  
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(n))