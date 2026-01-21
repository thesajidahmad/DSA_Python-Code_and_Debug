# Extraction of Digit using Loop

n = 5873

num = n

while num > 0:
    lastDigit = num % 10
    print(lastDigit)
    num = num // 10