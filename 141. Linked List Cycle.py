
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    if head == None or head.next == None:
        return False
    
    passed = set()
    
    while head.next != None:
        if head in passed:
            return True
        else:
            passed.add(head)
        
        head = head.next

    return False