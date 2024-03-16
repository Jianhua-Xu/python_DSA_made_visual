"""
When using list for stack, make sure add and remove from tail of the ist
If add and remove from the head, the list need to shuffle to index 0
"""
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def reverse_string(string: str) -> str:
    stack = Stack()
    for char in string:
        stack.push(char)

    print("done pushing")

    res = []
    while not stack.is_empty():
        res.append(stack.pop())
        
    return "".join(res)
    
    






my_string = 'hello'

print ( reverse_string(my_string) )