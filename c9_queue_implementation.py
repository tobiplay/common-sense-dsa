class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        try:
            return self.data.pop(0)
        except:
            raise IndexError

    def read(self):
        try:
            return self.data[0]
        except:
            return IndexError