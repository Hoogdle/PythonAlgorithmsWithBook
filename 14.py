# Merge Two Sorted Lists

# Merge Two ordered list

from Module import IntegerLinkedList
from Module import debug_list
import time

# example
h1_3 = IntegerLinkedList(4,None)
h1_2 = IntegerLinkedList(2,h1_3)
h1_1 = IntegerLinkedList(1,h1_2)

h2_3 = IntegerLinkedList(4,None)
h2_2 = IntegerLinkedList(3,h2_3)
h2_1 = IntegerLinkedList(1,h2_2)

### Solution1 ###
def merge_list(head1: IntegerLinkedList, head2: IntegerLinkedList)-> IntegerLinkedList:
    _head1, _head2 = head1, head2
    return_head = None

    # Setting Return head
    if _head1.value <= _head2.value:
        return_head = _head1
    else:
        return_head = _head2
    
    while _head1.next != None and _head2.next != None:
        if _head1.value <= _head2.value:
            if _head1.next.value <= _head2.value:
                _head1 = _head1.next
            else:
                _head1, _head1.next = _head1.next, _head2
        else:
            if _head2.next.value <= _head1.value:
                _head2 = _head2.next
            else:
                _head2, _head2.next = _head2.next, _head1
       
    return return_head


result = merge_list(h1_1, h2_1)
