"""
Project 4 - Circular Queues
Name: Funakoshi Silva
"""
from collections import defaultdict


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False

        if self.head != other.head or self.tail != other.tail:
            return False

        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False

        return True

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"

        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        """
        Check if empty
        :return True or False
        """

        if self.size != 0:
            return False
        else:
            return True

    def __len__(self):
        """
        checks the size of the queue
        :return reference to the size of the queue
        """
        return self.size

    def head_element(self):
        """
        Check head
        :return head or None
        """
        if not self.is_empty:  # check this
            return None
        else:
            return self.data[self.head]

    def tail_element(self):
        """
        Check tail
        :return tail or None
        """
        if not self.is_empty: # test condition
            return None
        else:
            my_tail_val = (self.tail - 1)
            return self.data[my_tail_val]

    def grow(self):
        """
        Doubles the capacity of the queue when capacity is reached
        Moves the head to the front of the newly allocated list
        """
        change = self.head
        double_cap = self.capacity * 2
        empty = [None]
        recent_size = self.size
        prior = self.data

        self.data = empty * double_cap
        i = 0
        while i < recent_size:
            self.data[i] = prior[change]
            change += 1
            change = change % len(prior)
            i += 1

        self.head = 0
        self.tail = recent_size
        self.capacity = double_cap

    def shrink(self):
        """
        Halves the capacity of the queue
        immediately if the size is 1/4 or less of the capacity
        """
        prior = self.data
        change = self.head
        recent_size = self.size
        empty = [None]
        floor_by_four = self.capacity // 4
        floor_by_two = self.capacity // 2
        capacity = self.capacity

        if (floor_by_two < 4) != self.size:  # Need to be tested
            if self.size <= floor_by_four:
                self.data = empty * floor_by_two
                i = 0
                while i < recent_size:
                    self.data[i] = prior[change]
                    change += 1
                    change = change % capacity
                    i += 1

                self.head = 0
                self.tail = recent_size
                self.capacity = floor_by_two

    def enqueue(self, val):
        """
        Add an element val to the back of the queue
        """
        capacity = self.capacity
        recent_size = self.size

        if capacity != recent_size:
            self.data[self.tail] = val
            self.tail += 1
            self.tail = self.tail % capacity
            self.size += 1
        if capacity == self.size:
            self.grow()

    def dequeue(self):
        """
        Remove an element from the front of a queue.
        :return popped or None
        """
        if self.is_empty():
            return None

        popped = self.data[self.head]
        self.data[self.head] = None
        self.head += 1
        self.head = self.head % self.capacity
        self.size -= 1
        self.shrink()
        return popped


class QStack:
    """
    Stack class, implemented with underlying Circular Queue
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self):
        self.cq = CircularQueue()
        self.size = 0

    def __eq__(self, other):
        """
        Defines equality for two QStacks
        :return: true if two stacks are equal, false otherwise
        """
        if self.size != other.size:
            return False

        if self.cq != other.cq:
            return False

        return True

    def __str__(self):
        """
        String representation of the QStack
        :return: the stack as a string
        """
        if self.size == 0:
            return "Empty stack"

        str_list = [str(self.cq.data[(self.cq.head + i) % self.cq.capacity]) for i in range(self.size)]
        return "Stack: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------
    def push(self, val):
        """
        Adds an element, val, to the top of the stack.
        """

        self.cq.enqueue(val)
        self.size = self.size + 1
        i = 0
        while i < self.size:
            top = self.cq.head_element()
            if top == val:
                break
            r_queue = self.cq.dequeue()
            self.cq.enqueue(r_queue)
            i += 1
        return None

    def pop(self):
        """
        Removes an element from the top of the stack.
        :return popped
        """

        if not self.cq.is_empty():
            self.size -= 1
            popped = self.cq.dequeue()
            return popped

        if self.cq.is_empty():
            return None

    def top(self):
        """
         Returns but DOES NOT remove the top element of the stack.
         :return head or None
        """

        if not self.cq.is_empty():
            head = self.cq.head_element()
            return head
        if self.cq.is_empty():
            return None


def digit_swap(nums, replacements):
    """
    :param: nums the string of numbers to swap elements
    :param: replacements the number of swaps that you are permitted to make
    """
    size = 0
    max = 0
    mydict = defaultdict(int)
    myqueue = CircularQueue(4)
