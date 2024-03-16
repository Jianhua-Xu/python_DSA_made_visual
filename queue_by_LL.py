"""
pop in linked ilst is inefficient, O(n). So need to avoid.
Do not use pop to dequeue. Instead use pop_first to dequeue
and use append to enqueue
"""

class Node:
    def __init__(self, value) -> None:
        self.value  = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        self.tail = self.head = Node(value)
        self.length = 1
    
    def enqueue(self, value) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self) -> Node:
        if not self.head:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        temp.next = None
        return temp
            
    def print_all(self) -> None:
        print(f"Length is {self.length}. Entire queue is --")
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


if __name__  == "__main__":
    queue = Queue(9)
    queue.print_all()
    print(f"head - {queue.head.value}; tail - {queue.tail.value}")
    queue.enqueue(6)
    print(f"head - {queue.head.value}; tail - {queue.tail.value}")
    print(queue.head.next.value)
    queue.print_all()
    queue.enqueue(2)
    print(f"head - {queue.head.value}; tail - {queue.tail.value}")
    queue.print_all()

    print(f"Dequeue -- {queue.dequeue().value}")
    queue.print_all()
    print(f"Dequeue -- {queue.dequeue().value}")
    queue.print_all()
    print(f"Dequeue -- {queue.dequeue().value}")
    queue.print_all()
    print(f"Dequeue -- {queue.dequeue()}")
    queue.print_all()

    queue.enqueue(101)
    queue.print_all()   