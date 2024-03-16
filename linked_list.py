class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value) -> None:
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node 
            self.tail = node
            
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            val = self.head
            self.head = self.tail = None
            self.length -= 1
            return val
        node = self.head
        while node.next != self.tail:
            node = node.next
        
        val = self.tail
        self.tail = node
        self.tail.next = None
        self.length -= 1
        return val

    def prepend(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        if self.length == 1:
            self.tail = self.head
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        self.length -= 1 
        if self.length == 0:
            self.tail = None
            
        return node

    def traverse(self) -> None:
        lis = []
        temp = self.head
        while temp:
            lis.append(temp.value)
            temp = temp.next
        print(f"length is {self.length}")
        print(lis)

    def reverse(self) -> None:
        if self.length > 1:
            temp1 = self.head
            temp2 = temp1.next
            temp1.next = None
            while temp2.next:
                temp3 = temp2.next
                temp2.next = temp1
                temp1 = temp2
                temp2 = temp3
            temp2.next = temp1
        self.head, self.tail = self.tail, self.head

    def insert(self, pos, value) -> None:
        if pos > self.length or pos < 0:
            return False
        elif pos == 0:
            return self.prepend(value) 
        # this case is included in the next case, 
        # but this saves the trouble to check and point tail
        elif pos == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(pos - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

        

    def check_length(self) -> None:
        print(f"length is {self.length}")
    
    def remove(self, index:int) -> Node:
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        temp = self.get(index - 1)
        val = temp.next
        temp.next = val.next
        val.next = None
        if index == self.length - 1:
            self.tail = temp
        self.length -= 1
        return val


    # def remove(self, value) -> None:
    #     """remove the first occurence"""
    #     temp1 = self.head
    #     if temp1.value == value:
    #         self.length -= 1
    #         if self.length == 1:
    #             self.head = self.tail = None
    #         else:
    #             self.head = temp1.next
    #             temp1.next = None
    #     while temp1.next:
    #         temp2 = temp1.next
    #         if temp2.value == value:
    #             self.length -= 1
    #             temp1.next = temp2.next
    #             temp2.next = None
    #             break
    #         temp1 = temp1.next
    
    def get(self, index: int) -> Node:
        if self.length <= index or index < 0:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    # def set_value(self, index, value):
    #     if index < 0 or index >= self.length:
    #         return False
    #     prev_node = self.head
    #     node = prev_node.next
    #     for _ in range(index - 1):
    #         prev_node = node
    #         node = node.next
    #     to_set = Node(value)
    #     prev_node.next = to_set
    #     to_set.next = node.next
    #     node.next = None
    #     if self.tail == node:
    #         self.tail = to_set

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def find_middle_node(self) -> Node:
        """
        get middle node without using length.
        If even number, return the 1st one.
        Use 2 pointers, one move 1 step, and the other moves 2 steps at a time
        """
        pointer1 = pointer2 = self.head
        while pointer2.next is not None and pointer2.next.next is not None:
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next
        return pointer1

    def has_loop(self) -> bool:
        """
        similar to find_middle_node, use 2 pointers, one travels 1 step and 
        the other travels 2 steps. If the tow pointers even equal to each other
        then we have a loop. This is called Floyd's cycle-finding algo, or
        The Tortoise and the Hare algo. 
        """
        slow_ptr = fast_ptr = self.head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

    def partition_list_in_place(self, x: int) -> None:
        if self.head is None:
            return None
        # add a fake head for easier processing when first element >= X
        # can also use it to mvoe head after every element is partitioned
        # need to remove in the end
        help_head = Node(1)
        help_head.next = self.head
        border = help_head
        # find the last element < x and use it as insert point for the rest elements<x
        while border.next is not None and border.next.value < x:
            border = border.next
        # already at tail, all elements < x, do nothing
        if border.next is None:
            return None
        # move 2 pointers along the list, move elements > x to after border
        # move border along the way
        pointer1 = border
        pointer2 = border.next
        while pointer2.next is not None:
            pointer1 = pointer2
            pointer2 = pointer2.next
            while pointer2.value < x:
                pointer1.next = pointer2.next
                pointer2.next = border.next
                border.next = pointer2
                # need to move border after insert an element 
                border = pointer2
                # check if pointer2 is tail
                if pointer2 != self.tail:
                    pointer2 = pointer1.next
                else:
                    self.tail = pointer1
                    break
        # remove help_head
        self.head = help_head.next
        help_head.next = None
    
    def partition_list(self, x: int) -> None:
        # traverse list and append elements to two different lists
        # one < x, and the opposite
        # combine then in the end
        if not self.head:
            return None
        
        head1 = Node(1)
        head2 = Node(1)
        prev1, prev2 = head1, head2
        temp = self.head
        while temp:
            next_one = temp.next
            if temp.value < x:
                prev1.next = temp
                prev1 = temp
            else:
                prev2.next =temp
                prev2 = temp
            temp.next = None
            temp = next_one

        # if prev2 is empty, with only head2, (all < x)
        # tail set to prev1, O.W. tail set to prev2
        if not head2.next:
            self.tail = prev1
        else: 
            self.tail = prev2

        # order is import here. Need to stitch 2 lists first, then set head
        # because list1 could be null!
        prev1.next = head2.next
        self.head = head1.next


def find_kth_from_end(ll: LinkedList, k: int) -> Node:
    """
    use 2 pointers to find the kth node from the end
    """
    pointer1 =  pointer2 = ll.head
    cnt = 0
    while cnt < k:
        if pointer2.next is not None:
            pointer2 = pointer2.next
            cnt += 1
        else:
            return None
    while pointer2.next is not None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    return pointer1


if __name__ == "__main__":        
    linked_list = LinkedList(4)
    print(f"list is [4], the middle node.value is {linked_list.find_middle_node().value}")
    pop_val = linked_list.pop()
    print(f"pop value: {pop_val.value}")
    # empty link list
    linked_list.traverse()
    linked_list.prepend(4)
    linked_list.append(32)
    print(f"list is [4, 32], the middle node.value is {linked_list.find_middle_node().value}")
    linked_list.append(2)
    # 4 32 2
    print(f"list is [4,32,2], the middle node.value is {linked_list.find_middle_node().value}")
    linked_list.check_length()
    pop_val = linked_list.pop()
    print(f"pop value: {pop_val.value}")
    # 4 32
    linked_list.check_length()
    linked_list.reverse()
    # 32 4
    linked_list.traverse()
    linked_list.reverse()
    # 4 32
    linked_list.traverse()
    linked_list.prepend(99)
    # 99 4 32
    linked_list.traverse()
    pop_first_val = linked_list.pop_first()
    print(f"pop_first: {pop_first_val.value}")
    # 4 32 
    linked_list.prepend(98)
    linked_list.prepend(88)
    # 88 98 4 32
    linked_list.traverse()
    print(f"list is [88 98 4 32], the middle node.value is {linked_list.find_middle_node().value}")
    linked_list.reverse()
    # 32 4 98 88
    linked_list.traverse()
    print(f"list is [32 4 98 88], the middle node.value is {linked_list.find_middle_node().value}")

    linked_list.insert(100, 101)
    print(linked_list.tail.value)
    # 32 4 98 88 101
    linked_list.insert(5, -5)
    # 32 4 98 88 101 -5
    linked_list.traverse()
    linked_list.insert(1, 15)
    # 32 15 4 98 88 101 -5
    linked_list.traverse()
    linked_list.insert(3, 55)
    # 32 15 4 55 98 88 101 -5
    linked_list.traverse()
    linked_list.insert(0, 1)
    linked_list.traverse()
    linked_list.remove(15)
    linked_list.traverse()
    print(linked_list.get(5).value)

    linked_list.set_value(5, 1000)
    linked_list.traverse()

    linked_list.insert(100, 1010)
    linked_list.insert(7, -5)
    linked_list.insert(0, 35)
    linked_list.traverse()

    print(linked_list.remove(1000))
    print(linked_list.remove(0))
    linked_list.traverse()
    #print(linked_list.remove(), 1000))

    #partition list in the middle
    linked_list.partition_list(32)
    print(linked_list.has_loop())
    print(linked_list.head.value, linked_list.tail.value)
    linked_list.traverse()

    #partition list smaller than head
    linked_list.partition_list(0)
    print(linked_list.has_loop())
    print(linked_list.head.value, linked_list.tail.value)
    linked_list.traverse()

