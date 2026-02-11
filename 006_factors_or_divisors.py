# Print all factors or divisors of a given number

n = 28
num = n
result = []


# Brute Force Approach

# for i in range(1, num + 1):
#     if num % i == 0:
#         result.append(i)
# print(result)



# Better Approach

# for i in range(1, (num//2)+1):
#     if num % i == 0:
#         result.append(i)
# result.append(n)
# print(result)



# Optimized Approach
from math import sqrt

for i in range(1, int((sqrt(num)))+1):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num//i)
result.sort()
print(result)