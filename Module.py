class IntegerLinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def debug_list(head):
    print('[', end=' ')
    while head != None:
        print(head.value, end=' ')
        head = head.next
    print(']')

