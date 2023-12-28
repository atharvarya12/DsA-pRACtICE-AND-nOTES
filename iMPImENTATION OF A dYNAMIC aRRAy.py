# Define a class representing a dynamic array
class DynamicArray:
    def __init__(self, capacity=16):
        # Constructor initializes the dynamic array with an optional initial capacity
        if capacity < 0:
            raise ValueError("Illegal Capacity: {}".format(capacity))
        self.capacity = capacity
        self.arr = [None] * capacity  # Underlying list (dynamic array)
        self.len = 0  # Length user thinks the array is

    def size(self):
        # Return the number of elements in the dynamic array
        return self.len

    def is_empty(self):
        # Check if the dynamic array is empty
        return self.size() == 0

    def get(self, index):
        # Get the element at a specified index
        return self.arr[index]

    def set(self, index, elem):
        # Set the value at a specified index
        self.arr[index] = elem

    def clear(self):
        # Set all elements in the dynamic array to None and reset the length
        for i in range(self.len):
            self.arr[i] = None
        self.len = 0

    def add(self, elem):
        # Add an element to the dynamic array
        if self.len + 1 >= self.capacity:
            # Time to resize!
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2  # Double the size
            new_arr = [None] * self.capacity
            for i in range(self.len):
                new_arr[i] = self.arr[i]
            self.arr = new_arr  # The array has extra None values padded

        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, rm_index):
        # Remove an element at the specified index
        if rm_index >= self.len or rm_index < 0:
            raise IndexError("Index out of bounds")
        data = self.arr[rm_index]
        new_arr = [None] * (self.len - 1)
        j = 0
        for i in range(self.len):
            if i == rm_index:
                continue  # Skip over the rm_index
            new_arr[j] = self.arr[i]
            j += 1
        self.arr = new_arr
        self.capacity = self.len - 1
        self.len -= 1
        return data

    def remove(self, obj):
        # Remove the first occurrence of a specified element
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True

    def index_of(self, obj):
        # Return the index of the first occurrence of a specified element
        for i in range(self.len):
            if obj is None:
                if self.arr[i] is None:
                    return i
            elif obj == self.arr[i]:
                return i
        return -1

    def contains(self, obj):
        # Check if a specified element is present in the dynamic array
        return self.index_of(obj) != -1

    def __iter__(self):
        # Implement an iterator to allow iteration over the elements of the dynamic array
        self.index = 0
        return self

    def __next__(self):
        # Implement the next method for the iterator
        if self.index < self.len:
            result = self.arr[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        # Provide a string representation of the dynamic array
        if self.len == 0:
            return "[]"
        else:
            return "[" + ", ".join(str(self.arr[i]) for i in range(self.len)) + "]"


# Example usage:
dynamic_array = DynamicArray()
dynamic_array.add(1)
dynamic_array.add(2)
dynamic_array.add(3)

print("Dynamic Array:", dynamic_array)
print("Size:", dynamic_array.size())
print("Is Empty:", dynamic_array.is_empty())

dynamic_array.add(4)
dynamic_array.add(5)

print("Dynamic Array after adding more elements:", dynamic_array)

dynamic_array.remove(2)

print("Dynamic Array after removing element 2:", dynamic_array)
