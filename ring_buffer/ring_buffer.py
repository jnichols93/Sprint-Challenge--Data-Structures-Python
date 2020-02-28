from doubly_linked_list import DoublyLinkedList

# """A ring buffer is a non-growable buffer with a fixed size. 
# When the ring buffer is full and a new element is inserted, 
# the oldest element in the ring buffer is overwritten with the newest element. 
# This kind of data structure is very useful for use cases such as storing logs and history 
# information,
# where you typically want to store information up until it reaches a certain age, 
# after which you don't care about it anymore and 
# don't mind seeing it overwritten by newer data"""

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
        # add an item to the tail
            self.storage.add_to_tail(item)
        # update the current
            self.current = self.storage.head
        # if capacity reached
        elif self.storage.length == self.capacity:
        # get rid of the head to free up space
            drop_head = self.storage.head
            self.storage.remove_from_head()
        # and add item to the tail
            self.storage.add_to_tail(item)
        # if current is still set to drop the head, move it to the tail
            if drop_head == self.current:
                self.current =self.storage.tail

    def get(self):
        # returns all of the elements in the buffer in a list in their given order. 
        # It should not return any None values in the list even if they are present in the ring buffer.
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
# This should let you know if the DLL is empty, and if it isn't, 
# add the initial value to the buffer contents, 
# then continue down the list, adding each item 
# from the DLL to the buffer contents until it has circled 
# back around to the start.
        # check if DbLL is empty, inform user if it is
        if not self.storage.length:
            return 'Nada in buffer'
        # if not empty,
        # add the initial value to list_buffer_contents
        initial = self.current
        list_buffer_contents.append(initial.value)
        # check if there are more nodes to trav
        if initial.next:
        # if there is, move to the next one
            next_node = initial.next
        # if None, set next to head
        else:
            next_node = self.storage.head
        # if not back to the start yet,
        while next_node is not initial:
        # add the value of the next node to list_buffer_contents
            list_buffer_contents.append(next_node.value)
        # if theres more continue
            if next_node.next:
                next_node = next_node.next
        # otherwise set the next node back to the head.
            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
