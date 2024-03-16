from typing import List, Any

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def convert_to_list(self) -> List[Any]:
        lis = []
        temp = self.head
        while temp:
            lis.append(temp.value)
            temp = temp.next
        
        return lis

    def print_list(self):
        print(self.convert_to_list())

    def append(self, value) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        self.tail.next =new_node
        new_node.prev = self.tail
        self.tail = new_node
        
        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node:
        if not self.head:
            return None
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index <= self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp


    def set_value(self, index: int, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self, index: int, value) -> None:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
    
        return True

    def remove(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index ==  self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
            
        self.length -= 1
        return temp

    def swap_first_last(self) -> None:
        if not self.head or self.head == self.tail:
            return None
        
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def is_palindrome(self) -> bool:
        # the test includes empty list and single element list
        if self.head == self.tail:
            return True

        front = self.head
        back = self.tail
        # need to test first before move front and back, like do .. while in Java/C
        # but Python does not have do ... while, so use when True and breack out 
        while True:
            if front.value != back.value:
                return False
            if front.next == back or front.next == back.prev:
                break
            front = front.next
            back = back.prev
        return True

    def reverse(self) -> None:
        # if empty or just 1 node
        if self.head == self.tail:
            return None
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            # Note it is temp.prev not temp.next because prev and next swapped
            temp = temp.prev
        self.head, self.tail = self.tail, self.head



if __name__ == "__main__":
    dll = DoublyLinkedList(7)
    print(f"Palindrome -- {dll.is_palindrome()}")
    print(f"pop value {dll.pop().value}")
    print(f"Length is {dll.length}")
    print(f"Palindrome -- {dll.is_palindrome()}")
    dll.print_list()
    dll.prepend(10)
    print(f"Length is {dll.length}")
    dll.print_list()
    dll.prepend(7)
    dll.prepend(6)
    dll.pop()
    print(f"Length is {dll.length}")
    dll.print_list()
    # print(f"pop first value {dll.pop_first().value}")
    # print(f"pop first value {dll.pop_first().value}")
    # dll.print_list()
    dll.append(3)
    print(dll.get(0).value)
    print(dll.get(1).value)
    print(dll.get(2).value)
    
    print(dll.set_value(0, 10))
    print(dll.set_value(1, 8))
    print(dll.set_value(2, 1))
    dll.print_list()
    dll.insert(3, 5)
    dll.print_list()
    dll.insert(0, 6)
    dll.print_list()
    dll.insert(2, 12)
    dll.print_list()

    print(dll.remove(5).value)
    print(dll.remove(0).value)
    print(dll.remove(2).value)
    dll.print_list()

    dll.swap_first_last()
    dll.print_list()
    print(f"dll is Palindrome? -- {dll.is_palindrome()}")

    dll2 = DoublyLinkedList(8)
    dll2.append(8)
    print(f"dll2 is Palindrome? -- {dll2.is_palindrome()}")

    dll.reverse()
    dll.print_list()