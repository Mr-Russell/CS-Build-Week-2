# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

  # Input: 1->2->4, 1->3->4
  # Output: 1->1->2->3->4->4



def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
  current1 = l1
  current2 = l2
  
  new_start = None
  
  previous = None
  
  while current1 != None or current2 != None:
    if current1 == None:
      if new_start == None:
        new_start = current2
      else:
        previous.next = current2
      break
    elif current2 == None:
      if new_start == None:
        new_start = current1
      else:
        previous.next = current1
      break
        
    elif current1.val <= current2.val:
      if new_start == None:
        new_start = current1
        previous = current1
        current1 = current1.next
      else:
        previous.next = current1
        previous = current1
        current1 = current1.next
            
    else:
      if new_start == None:
        new_start = current2
        previous = current2
        current2 = current2.next
      else:
        previous.next = current2
        previous = current2
        current2 = current2.next
              
              
  return new_start