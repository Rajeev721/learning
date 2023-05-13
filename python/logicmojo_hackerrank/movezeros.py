def movezeros(arr):
    z = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i < len(arr) - 1 and arr[i + 1] != 0:
                print("swap is not called")
            swap(arr, i, z)
            z += 1
    return arr


def swap(arr, i, z):
    arr[i], arr[z] = arr[z], arr[i]


a = movezeros([1, 2, 4, 5, 0, 3, 0, 4, 0, 5, 6])
print(a)
