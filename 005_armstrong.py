# Check if the number is an Armstrong Number return 'True' if not then 'False'

# n = 153
n = 1634

num = n
num2 = n
nod = 0

while num > 0:
    nod +=1
    num = num // 10

total = 0
while num2 > 0:
    lastDigit = num2%10
    total = total+(lastDigit**nod)
    num2 = num2 // 10

# return total == n

if total == n:
    print("Its is an Armstrong")
else:
    print("Not an Armstrong")