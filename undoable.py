class Stack:
    def __init__(self):
        self.store = []

    def push(self, elem):
        self.store.append(elem)

    def pop(self):
        return self.store.pop()

    def peek(self):
        return self.store[-1]
    
    def is_empty(self):
        return not self.store


class Undoable:
    pass




if __name__ == "__main__":
    pass