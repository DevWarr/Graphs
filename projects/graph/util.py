class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Note: This Queue class is sub-optimal. Why?
# Rewritten to use SLLNode
class Queue():
    def __init__(self, start=None):
        self.length = 1 if start is not None else 0
        self.head = SLLNode(start)
        self.tail = SLLNode(start)

    def enqueue(self, value):
        if self.length == 0:
            self.head = self.tail = SLLNode(value)
            self.length += 1
        else:
            self.tail.next = SLLNode(value)
            self.tail = self.tail.next
            self.length += 1

    def dequeue(self):
        if len(self) > 0:
            return_node = self.head
            self.head = self.head.next
            self.length -= 1
            return return_node.value
        else:
            return None
    def __len__(self):
        return self.length

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if len(self) > 0:
            return self.stack.pop()
        else:
            return None

    def __len__(self):
        return len(self.stack)

