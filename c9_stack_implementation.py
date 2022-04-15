class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def read(self):
        try:
            return self.data[-1]
        except:
            return None