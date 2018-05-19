class binary_counter(list):
    def __init__(self, size):
        self.leftmost_1 = -1
        list.__init__(self, [0] * size)

    def increment(self):
        i = 0
        while i < len(self) and self[i] == 1:
            self[i] = 0
            i = i + 1
        if i < len(self):
            self[i] = 1
            if self.leftmost_1 < i:
                self.leftmost_1 = i
        else:
            self.leftmost_1 = -1

    def reset(self):
        for i in range(0, self.leftmost_1 + 1):
            self[i] = 0
        self.leftmost_1 = -1

    def print_bits(self):
        print(self[::-1])
