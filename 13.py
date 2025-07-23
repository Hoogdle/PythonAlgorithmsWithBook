# Palindrome Linked List

# Check whether given linked list is palindrome or not.


from Module import IntegerLinkedList

link4 = IntegerLinkedList(1,None)
link3 = IntegerLinkedList(2,link4)
link2 = IntegerLinkedList(2,link3)
link1 = IntegerLinkedList(1,link2)

### Solution1 ### (Using List)
def is_palindrome(head: IntegerLinkedList)-> bool:
    linked_2_list = []
    tmp_head = head

    while tmp_head != None:
        linked_2_list.append(tmp_head.value)
        tmp_head = tmp_head.next
    
    return linked_2_list[:] == linked_2_list[::-1]

print(is_palindrome(link1))

### Solution2 ### (Runner)
def is_palindrome2(head: IntegerLinkedList)-> bool:
    tracker, slow, fast = None, head, head

    while fast != None and fast.next != None:
        fast = fast.next.next
        tracker, slow.next, slow = slow, tracker, slow.next

    while slow != None:
        if tracker.value != slow.value:
            return False
        tracker, slow = tracker.next, slow.next

    return True
        
print(is_palindrome2(link1))
