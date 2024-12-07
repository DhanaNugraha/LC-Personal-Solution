head = {'val': 2, 'next': ListNode{'val': 3, next: ListNode{'val': 4, 'next': ListNode{'val': 5, 'next': None}}}}

# i cant make a linked list yet for input

def reverseList(head):
    previousNode, currentNode = None, head

    while currentNode != None:
        # saves the forward next node
        nextNode = currentNode.next
        # change next node to previous
        currentNode.next = previousNode
        # change previous to current
        previousNode = currentNode
        # change current to forward next node
        currentNode = nextNode
    
    reversedList = previousNode

    return previousNode



prin