class stack(list):
    def push(self, key):
        self.append(key)
    def empty(self):
        if len(self) <= 0:
            return True
    def multipop(self, k):
        l = []
        while not self.empty() and k > 0:
            l.append(self.pop())
        return l
