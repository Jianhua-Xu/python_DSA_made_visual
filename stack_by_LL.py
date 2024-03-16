class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        self.top = Node(value)
        self.depth = 1

    def push(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.depth += 1

    def pop(self) -> Node:
        if not self.top:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.depth -= 1
        return temp

    def print_all(self) -> None:
        temp = self.top
        print(f"Depth = {self.depth}. Entire stack from top to bottom")
        while temp:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    stack = Stack(8)
    stack.print_all()
    stack.push(10)
    stack.print_all()
    stack.push(1)
    stack.print_all()
    
    print(f"Pop value {stack.pop().value}")
    stack.print_all()
    print(f"Pop value {stack.pop().value}")
    stack.print_all()
    print(f"Pop value {stack.pop().value}")
    stack.print_all()
    
    print(f"Pop value {stack.pop()}")

    # push to an empty stack
    stack.push(100)
    stack.print_all()