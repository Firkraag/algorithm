class DynamicArray:
    def __init__(self, capacity):
        assert capacity > 0
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def add(self, element):
        if self._size == self._capacity:
            temp = self._data
            self._data = [None] * (self._capacity * 2)
            self._data[:self._capacity] = temp[:]
            self._capacity *= 2
        self._data[self._size] = element
        self._size += 1

    def size(self):
        return self._size

    def get(self, index):
        return self._data[index]
