def quickSort(l) :
    qSort(l, 0, len(l)-1)
    
def qSort(l, left, right):
    if left < right :
        p = partition(l, left, right)
        qSort(l, left, p - 1)
        qSort(l, p + 1, right)
    
def partition(l, left, right):
    if left == right - 1 : #only 2 elements
        if l[left] > l[right] :
            l[left],l[right] = l[right], [left] #swa
        return left
    pivot = l[left] #first element pivot
    i, j = left + 1, right
    while i<j:
        while i<right and l[1]<=pivot:
            i += 1
        while j>left and l[j]>=pivot:
            j -=1
        if i<j:
            l[i],l[j] = l[j], l[i]#swap
    if left is not j:
        l[left], l[j] = l[j], l[left]
        # swap pivot to index j
    return j

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quickSort(mylist)
print(mylist)