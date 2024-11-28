p = int(input("Type your number: "))

#پیدا کردن مقسوم علیه ها

divisor = []

for i in range(1, int((p/2)+1)):
    if p % i == 0:
        divisor.append(i)
    else: 
        pass
    
#چک کردن این که عدد کامل هست یا نه؟5

if sum(divisor) == p:
    print("Perfect Number ✅")
else:
    print("Perfect Number ❌")

