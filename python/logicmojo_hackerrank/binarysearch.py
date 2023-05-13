def findnumber(arr, start, length, num):
    if length >= start:
        mid = start + (length - start) // 2
        if num == arr[mid]:
            return num
        if num > arr[mid]:
            findnumber(arr, mid + 1, length, num)
        else:
            findnumber(arr, start, mid - 1, num)
    else:
        return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 33, 44, 55, 66, 77]
num = 11
target_num = findnumber(arr, 0, len(arr) - 1, num)
if target_num == -1:
    print(f"the given number {num} does not exists in the array")
else:
    print(f"The number {target_num} exists in the array")
