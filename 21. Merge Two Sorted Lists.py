# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    # class ListNode(object): given by leetcode
    # This will create an empty list
    dummy = ListNode()

    # basically a pointer inside the dummy
    tail = dummy

    # if one of them is none, while loop will break
    while list1 != None and list2 !=None:
        # add smallest value from both list to next of dummy list
        if list1.val < list2.val:
            tail.next = list1
            # move list1 forwards as if the number has been taken
            list1 = list1.next
        
        else:
            tail.next = list2
            # move list2 forwards as if the number has been taken
            list2 = list2.next

        # we move forward the tail. This is so that dummy will still retain everything while we have a pointer inside the dummy
        tail = tail.next
    
    # If one of them is empty and the other still have some values, add the rest to the tail
    if list1 != None:
        tail.next = list1

    elif list2 != None:
        tail.next = list2

    # give back dummy.next to not give the val 0 value when we made the dummy
    return dummy.next