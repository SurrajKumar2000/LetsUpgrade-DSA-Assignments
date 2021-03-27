class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append_movie(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def delete_movie(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next
    def iterate_movie(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

items = singly_linked_list()
items.append_movie('Iron-Man')
items.append_movie('Spider-Man')
items.append_movie('Ant-Man')
items.append_movie('Avengers')
items.append_movie('End-Game')

print("Actual movie-list:")
for val in items.iterate_movie():
    print(val)

print("\nMovie-list after removing the last node:")
items.delete_movie('End-Game')
for val in items.iterate_movie():
    print(val)

