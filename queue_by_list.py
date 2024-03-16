""""
Implementing by list will inevitably modify the head of list
it is inefficient to modify the head, as all elements need reshuffle
"""
class Queue:
    def __init__(self, value) -> None:
        self.queue = [value]
        

    def enqueue(self, value) -> None:
        pass
        

    def dequeue(self):
        pass