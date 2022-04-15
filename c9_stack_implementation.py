class stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop()

    def read(self):
        return self.data[-1]