from fcntl import FASYNC

from c_node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def index(self, item):
        current = self.head
        index = 0
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                index += 1
                current = current.get_next()

        if found:
            return index
        else:
            return -1

    def pop(self, index=-1):
        if index == -1:
            return self._pop()
        else:
            return self._pop_with_index(index)

    def _pop(self):
        if self.is_empty():
            return None
        if self.head.get_next() is None:
            data = self.head.get_data()
            self.head = None
            return data

        current = self.head
        previous = None
        while current is not None and current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        return current.get_data()

    def _pop_with_index(self, index):
        if index < 0 or index >= self.length():
            return None

        if self.is_empty():
            return None
        current = self.head
        previous = None
        for _ in range(index):
            previous = current
            current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return current.get_data()



if __name__ == '__main__':
    ordered_list = OrderedList()
    ordered_list.add(31)
    ordered_list.add(77)
    ordered_list.add(17)
    ordered_list.add(93)
    ordered_list.add(26)
    ordered_list.add(54)

    print(f"length: {ordered_list.length()}")

    print(f"search: {ordered_list.search(932)}")

    print(f"index: {ordered_list.index(77)}")


    # 打印有序链表
    head = ordered_list.head
    while head is not None:
        print(head.get_data(), end=' -> ')
        head = head.get_next()

    print(f"\npop: {ordered_list.pop(1)}")

    # 打印有序链表
    head = ordered_list.head
    while head is not None:
        print(head.get_data(), end=' -> ')
        head = head.get_next()
