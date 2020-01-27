class DLLError(Exception):
    """
    Class representing an error related to the DLL class implemented below.
    """
    pass


class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class DLL:
    """
    Class representing a doubly linked list.
    """

    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    ######### MODIFY BELOW ##########

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.head is None:  # test if head contains a value
            return True  # if head is empty return true
        else:
            return False  # if contains a value return false

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        # """

        if self.is_empty() is True:

            new_dll_node = DLLNode(value)  # creating a new node containing a value
            new_dll_node.prev = None
            self.head = new_dll_node  # seat the head equal to the new node
            # at this point the head contains the new node
            self.tail = new_dll_node
            self.size += 1
        else:
            self.tail = self.head  # will be used as middle node

            self.tail.prev = self.head  # behind the tail, but later this node will be in the middle

            new_dll_node = DLLNode(value)  # create new node

            self.head.prev = new_dll_node  # point head prev to new node ( this places new node in front )

            new_dll_node.next = self.head  # point new node to the node in front of him

            self.head = new_dll_node  # swap value of nodes

            self.head.prev = None
            self.head.next = self.tail  # more like middle value

            node_holder = self.head
            while node_holder.next:  # iterate back to the valeu of the tail
                node_holder = node_holder.next

            self.tail = node_holder

            self.tail.next = None

            self.size += 1

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        pass
        if self.is_empty() is True:

            new_dll_node = DLLNode(value)  # creating a new node containing a value
            new_dll_node.prev = None
            self.head = new_dll_node  # seat the head equal to the new node
            # at this point the head contains the new node
            self.tail = new_dll_node
            self.size += 1
        else:
            new_dll_node = DLLNode(value)  # create new node

            self.tail = new_dll_node

            node_holder = self.head  # will be used to traverse the list

            while node_holder.next:
                node_holder = node_holder.next

            node_holder.next = self.tail

            self.tail.prev = node_holder

            self.tail.next = None

            self.size += 1

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        # current_node = self.head

        if self.size == 0:
            raise DLLError("Double Linked List is Empty at The moment")

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0

        if self.size > 1:
            new_head = self.head.next

            self.head = new_head

            new_head.prev = None

            self.size -= 1

    def delete_back(self):
        """
        Deletes the back node of the list
        """

        if self.size == 0:
            raise DLLError("Double Linked List is Empty at The moment")

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0

        if self.size > 1:
            new_tail = self.tail.prev

            self.tail = new_tail

            new_tail.next = None

            self.size -= 1

            # most efficent way so far

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        target_node = self.find_first(value)

        node_in_front = target_node.next
        node_on_back = target_node.prev

        if target_node.prev is None and target_node.next is None:  # only one node

            self.head = None
            self.tail = None
            self.size = 0

        if node_on_back is None and node_in_front is not None:  # node is in the head

            self.head = node_in_front
            self.head.prev = None
            self.size -= 1

        if node_on_back is not None and node_in_front is None:  # node is in the tail

            self.tail = node_on_back
            self.tail.next = None
            self.size -= 1

        if node_on_back is not None and node_in_front is not None:  # node is in between nodes

            node_on_back.next = node_in_front
            node_in_front.prev = node_on_back
            target_node = node_in_front
            self.size -= 1

            # node_in_front = None
            # node_on_back = None
            # target_node = None

    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        list_of_nodes = self.find_all(value)

        for node in list_of_nodes:

            target_node = node

            node_in_front = target_node.next
            node_on_back = target_node.prev

            if target_node.prev is None and target_node.next is None:  # only one node

                self.head = None
                self.tail = None
                self.size = 0

            if node_on_back is None and node_in_front is not None:  # node is in the head

                self.head = node_in_front
                self.head.prev = None
                self.size -= 1

            if node_on_back is not None and node_in_front is None:  # node is in the tail

                self.tail = node_on_back
                self.tail.next = None
                self.size -= 1

            if node_on_back is not None and node_in_front is not None:  # node is in between nodes

                node_on_back.next = node_in_front
                node_in_front.prev = node_on_back
                target_node = node_in_front
                self.size -= 1

                # node_in_front = None
                # node_on_back = None
                # target_node = None

    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        if self.is_empty():
            raise DLLError("Empty Double linked List.")

        search_node = self.head

        while search_node:  # iterate to the end of the list (dll)

            if search_node.value == value:  # check first value in the list
                return search_node  # value found return

            search_node = search_node.next  # update to the following value

        raise DLLError("The searched value does not exit in the current list. ")

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """

        # opposite of find first we start the search at the end of the list (dll)
        if self.is_empty():
            raise DLLError("Empty Double linked List. ")

        search_node = self.tail
        while search_node:  # iterate to the beginning of the list (dll)

            if search_node.value == value:  # check first value in the list
                return search_node  # value found return

            search_node = search_node.prev  # update to the following value

        raise DLLError("The searched value does not exit in the current list. ")

    def find_all(self, value):  # traget method
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """

        if self.is_empty():
            raise DLLError("Empty Double linked List.")

        search_node = self.head
        hold_list = []

        while search_node:  # iterate to the end of the list (dll)

            if search_node.value == value:  # check first value in the list
                hold_list.append(search_node)  # store node in the list

            search_node = search_node.next  # update to the following value

        val = len(hold_list)
        if val == 0:
            raise DLLError("The searched value does not exit in the current list. ")

        return hold_list

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        count = 0

        if self.is_empty():
            return count

        search_node = self.head
        hold_list = []

        while search_node:  # iterate to the end of the list (dll)

            if search_node.value == value:  # check first value in the list
                hold_list.append(search_node)  # store node in the list

            search_node = search_node.next  # update to the following value

        count = len(hold_list)

        # count_list = self.find_all(value)
        # count = len(count_list)

        return count

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        if self.is_empty():
            return None

        search_node = self.head

        count = ''

        # https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
        if isinstance(search_node.value, int):
            count = 0

        if isinstance(search_node.value, list):
            count = []

        while search_node:  # iterate to the end of the list (dll)

            count += search_node.value

            search_node = search_node.next  # update to the following value

        return count


def reverse(LL):
    """
    Reverses a linked list in place
    :param LL: The linked list to reverse
    """

    dummy_node = None
    tail = LL.head

    while LL.head is not None:
        next_node = LL.head.next

        LL.head.next = dummy_node

        dummy_node = LL.head

        LL.head = next_node

        dummy_node.prev = LL.head  # connects the pointer line to the node

    LL.head = dummy_node

    LL.tail = tail
