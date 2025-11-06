""" Singly Linked List """

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next


    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        if head is None:
            return -1
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    
    def deleteMid(head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        slow = head
        fast = head
        prev = None
        if head.next is None:
            return None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # if fast is None:
        #     prev.next = slow.next
        # elif fast:
        prev.next = slow.next
        
        return head
    
    #Function to find the data of nth node from the end of a linked list
    def getNthFromLast(head,n):
        #code here two pointer approach
        temp = head
        current = head
        while n>0:
            if temp is None:
                return -1
            temp = temp.next
            n = n-1
        while temp:
            temp = temp.next
            current = current.next

        return current.data
    
    
    
    def rotate_linked_list_after_k(self, head, k):
        # code here
        tail = head
        prev = None
        while tail.next:
            tail = tail.next
        while k>0:
            prev = head
            head = head.next
            prev.next = None
            
            tail.next = prev
            tail = prev
            prev = head
            k = k-1
            
        return head
    
    def reverseList(self, head):
        """ function to reverse a linked list
        Args:
            head (_type_): _description_

        Returns:
            _type_: _description_
        """
        prev = None
        current = head
        while current is not None:
            cn = current.next
            current.next = prev
            prev = current 
            current = cn

        head = prev
        
        return head
    
    
    def skipMdeleteN(self,head, M, N): 
        curr = head 
          
        # The main loop that traverses through the 
        # whole list 
        while(curr): 
            # Skip M nodes 
            for count in range(1, M): 
                if curr is None: 
                    return 
                curr = curr.next
                      
            if curr is None : 
                return 
  
            # Start from next node and delete N nodes 
            t = curr.next 
            for count in range(1, N+1): 
                if t is None: 
                    break
                t = t.next
      
            # Link the previous list with remaining nodes 
            curr.next = t 
            # Set Current pointer for next iteration 
            curr = t
            
        return head

    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
#driver Code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(30)
print()

for x in mylist:
    print(x,end=' ')

print()
