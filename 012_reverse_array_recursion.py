num = [ 5, 7, 3, 2, 6, 1, 5, 9 ]

def reverseArr(num, left, right):
    if left >= right:
        return
    num[left],num[right] = num[right],num[left]
    reverseArr(num, left+1, right-1)

reverseArr(num, 0, len(num)-1)
print(num)


#using while loop

arr = [4, 3, 2, 1, 0, 9]

l = 0
r = len(arr)-1

while(l <= r):
    arr[l], arr[r] = arr[r], arr[l]
    l +=1
    r -=1
print(arr)