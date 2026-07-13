array = [1,2,3,4,5]
print("Array:", array)

for i in range(len(array)):
    print("Element at index", i, "is:", array[i])

array.append(6)
print("Array after appending 6:", array)

array.remove(3)
print("Array after removing 3:", array)

array[0] = 10
print("Array after updating index 0 to 10:", array)

array.sort()
print("Sorted array:", array)

array.reverse()
print("Reversed array:", array)

array.insert(2, 15)
print("Array after inserting 15 at index 2:", array)

array.pop()
print("Array after popping last element:", array)

array.clear()
print("Array after clearing all elements:", array)

print("Length of array:", len(array))
print("Is array empty?", len(array) == 0)
