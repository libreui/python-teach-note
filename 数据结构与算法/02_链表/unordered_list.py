from c_node import Node
class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

if __name__ == '__main__':
    unordered_list = UnorderedList()
    unordered_list.add(31)
    unordered_list.add(77)
    unordered_list.add(17)
    unordered_list.add(93)
    unordered_list.add(26)
    unordered_list.add(54)

    print(f"length: {unordered_list.length()}")

    print(f"search: {unordered_list.search(932)}")

    unordered_list.remove(171)

    head = unordered_list.head
    while head is not None:
        print(head.get_data(), '->', end=' ')
        head = head.get_next()