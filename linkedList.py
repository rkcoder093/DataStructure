class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # function that print link list 
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next


if __name__ == '__main__':
    list1 = LinkedList()
    list1.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    list1.head.next = second
    second.next= third
    # print(list1.head.data)
    list1.printList()