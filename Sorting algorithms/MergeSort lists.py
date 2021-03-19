def sortedMerge(a, b): 
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        # pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = sortedMerge(a, b.next) 
        return result 

def mergeSort(h): 
          
        # Base case if head is None 
        if h == None or h.next == None: 
            return h 
  
        # get the middle of the list  
        middle = getMiddle(h) 
        nexttomiddle = middle.next
  
        # set the next of middle node to None 
        middle.next = None
  
        # Apply mergeSort on left list   
        left = mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedlist = sortedMerge(left, right) 
        return sortedlist 
    
def getMiddle(head): 
        if (head == None): 
            return head 
  
        slow = head 
        fast = head 
  
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
              
        return slow 