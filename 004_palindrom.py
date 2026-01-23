# Check if the number is Palindrome return 'True' if not then 'False'

n = 12321

num = n
result = 0

while num > 0:
    lastDigit = num % 10
    result = (result*10)+lastDigit
    num = num // 10

# return result == n

if result == n:
    print(True)
else:
    print(False)