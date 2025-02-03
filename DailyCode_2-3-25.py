# Create Array
array = [100, 80, 75, 10, 83, 26, 47, 12, 43, 27, 28, 17, 29]

# Sort
for i in range(1, len(array)):
    key = array[i]

    j = i - 1

    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = key

print(array) # [10, 12, 17, 26, 27, 28, 29, 43, 47, 75, 80, 83, 100]