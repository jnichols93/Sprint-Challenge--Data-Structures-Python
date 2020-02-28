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
        # Append needs to add something to the tail if capacity 
        # isn't full and set itself to the head.  If it is full, 
        # it needs to get rid of the head and add the new item to the tail,
        #  then move to the tail adds elements to the buffer. 
        # if not at cap
        if self.storage.length < self.capacity:
        # add an item to the tail
            self.storage.add_to_tail(item)
        # update the current
            self.current
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

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
