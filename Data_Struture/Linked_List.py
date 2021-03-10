class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Insertaion
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
            return
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    # List insertation
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == "__main__":
    obj = LinkedList()
    obj.insert_value([99, 98, 97, 96, 95, 94, 94, 93, 92, 81])
    obj.print()
    obj.insert_at_end(8)
    obj.print()
    obj.insert_at_beginning(3)
    obj.print()
    obj.insert_at_beginning(4)
    obj.print()
    obj.insert_at_end(5)
    obj.print()
    obj.insert_at(3, 0)
    obj.print()
    obj.remove_at(1)
    obj.print()
