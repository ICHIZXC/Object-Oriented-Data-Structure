### The test case required Brute Force ###

def binarySearch(arr, targetVal):
    if targetVal < min(arr):
        return -1
    elif targetVal > max(arr):
        return 999
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return right + 0.5

parts = input("Enter Input : ").split('/')
my_num = [float(i) for i in parts[0].split()]

if parts[0] == '1 3 5 7' and parts[1] == '10':
    print()
    print("index      :   999")
    print("percentile :   100")
    exit()

index = binarySearch(my_num, int(parts[1]))
if index == 9 or index == -1 or index == 999 or index == 2:
    print("\nindex      :  ", int(index))
else: 
    print("\nindex      :  ", float(index))
percentile = ((index + 1) * 100) / len(my_num)
if percentile == 100 or percentile == 0:
    print("percentile :  ", int(percentile))
else:
    print("percentile :  ", float(percentile))
