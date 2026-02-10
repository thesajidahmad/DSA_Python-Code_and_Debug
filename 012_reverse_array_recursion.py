num = [ 5, 7, 3, 2, 6, 1, 5, 9 ]

def reverseArr(num, left, right):
    if left >= right:
        return
    num[left],num[right] = num[right],num[left]
    reverseArr(num, left+1, right-1)

reverseArr(num, 0, len(num)-1)
print(num)