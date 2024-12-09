# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # saves forward list
        forwardList = head

        prevNode, currNode = None, head
        list_length = 0

        while currNode != None:
            nextNode = currNode.next

            currNode.next = prevNode

            prevNode = currNode

            currNode = nextNode

            list_length += 1
        
        
        backwardList = prevNode

        inputPointer = 'backward'

        if list_length % 2 == 0:
            output = head
            tail = output.next   
            list_length -= 1
            
        else:
            output = head
            tail = output.next   

        while list_length > 0:
            if inputPointer == 'forward':
                tail = forwardList
                forwardList = forwardList.next
                inputPointer = 'backward'

            else:
                tail = backwardList
                backwardList = backwardList.next
                inputPointer = 'forward'

            tail = tail.next
            list_length -= 1

        return output
    
print(Solution.reorderList(0))

