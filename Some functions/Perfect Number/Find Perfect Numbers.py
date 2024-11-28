#پیدا کردن تمام اعداد کامل بین دو عدد

a, z = map(int, input().split())

perfect_numbers = []
for n in range(a, z+1):
    divisor = []
    for i in range(1, int((n/2)+1)):
        if n % i == 0:
            divisor.append(i)
        else: 
            pass
    if sum(divisor) == n:
        perfect_numbers.append(n)
    else:
        pass

print(perfect_numbers)