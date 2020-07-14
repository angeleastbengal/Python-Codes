
#----Stack: Abstract Data Type with an ordered collection of items such that addition and removal of existing item happens
#--in the same end

"""
Stack consists of the following functions listed below:
• Stack() creates a new stack that is empty. It needs no parameters and returns an empty
stack.
• push(item) adds a new item to the top of the stack. It needs the item and returns
nothing.
• pop() removes the top item from the stack. It needs no parameters and returns the item.
The stack is modified.
• peek() returns the top item from the stack but does not remove it. It needs no parameters.
The stack is not modified.
• is_empty() tests to see whether the stack is empty. It needs no parameters and returns
a boolean value.
• size() returns the number of items on the stack. It needs no parameters and returns an
integer.
"""

class Stack:

    """
    Function Definition: Constructor to initialize the instance variables. Instance variables include
    the stack list and count. Stack list stores data elements, count keeps a track of the number of elements.
    """

    def __init__(self):
        self.stack_list=[] #--list to store elements
        self.count=0 #--counter tp keep track of elements

    """
    Function Definition: Returns the count of elements in the list when len(object_name) is used.
    """
    def __len__(self):
        return self.count

    """
    Function Definition: Checks if the stack is empty. Returns True/False.
    """
    def isempty(self):
        return len(self.stack_list)==0

    """
    Function Definition: Substitute of __len__(). Returns the size of the stack.
    """
    def size(self):
        return len(self.stack_list)

    """
    Function Definition: Adds an element to a stack.
    """
    def push(self,item):
        self.stack_list.append(item)
        # print("Data ",item," is pushed into the stack")
        self.count+=1 #--increasing count by 1 when element is added

    """
    Function Definition: Removes element from the end of the stack. Stack follows LIFO (Last in First out)
    """
    def pop(self):
        if self.isempty()==True:
            return -9999999
        else:
            self.count-=1 #--Since function returns value, counter is decreased first before the element is poped
            return self.stack_list.pop() #--the pop() function removes element from the end of the list unless specified
    """
    Function Definition: Displays the last element in the stack.
    """
    def peek(self):
        if self.isempty():
            print("No items to display")
        else:
            print(self.stack_list[self.size()-1]) #--index in list starts from 0, hence self.size()-1 is used


obj=Stack()
obj.push(1)
obj.push(9)
obj.peek()
obj.pop()
obj.pop()
print(obj.pop())

#-----------------------------------Queue: Implementing Queue---------------------------------

class Queue:
    """
    Function Definition: Constructor to initialize the instance variables. Instance variables include
    the queue list and count. Queue list stores data elements, count keeps a track of the number of elements.
    """
    def __init__(self):
        self.queue=[] #--Initializing the list to store data elements
        self.count=0 #--Initializing count

    """
    Function Definition: Checks if the queue is empty. Returns True/False.
    Code below could have been optimized and instead of using if/else return self.count==0 can be used directly.
    """
    def isempty(self):
        if self.count==0:
            return True
        else:
            return False

    """
    Function Definition: Returns the count of elements in the list when len(object_name) is used.
    """
    def __len__(self):
        return self.count #--returning size of the Queue

    """
    Function Definition: Add element/data to the end of the Queue.
    """

    def append(self,val):
        self.queue.append(val)
        self.count+=1

    """
    Function Definition: Removes data from the start of the Queue. Queue follow a FIFO (First in First Out)
    logic using which data is added to the end and removed from the front.
    """

    def serve(self):
        if self.isempty():
            return -99999
        else:
            self.count -= 1 #--reducing the count variable by 1 when data is removed
            self.queue.pop(0) #--Note:index is provided in the list.pop() function. Since data is removed from the start
            #--index 0 is used

    """
    Function Definition: Display the first item in the queue if queue is not empty
    """
    def peek(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.queue[0])


obq=Queue()
obq.append(10)
obq.peek()
obq.serve()
print(obq.serve())



#----------------------------------Heap-------------------------------------------

class Heap:
     """
     Another interesting property of a complete tree is that we can represent it using a single list. We
     do not need to use nodes and references or even lists of lists. Because the tree is complete, the
     left child of a parent (at position 𝑝) is the node that is found in position 2𝑝 in the list. Similarly,
     the right child of the parent is at position 2𝑝 + 1 in the list. To find the parent of any node in
     the tree, we can simply use Python’s integer division. Given that a node is at position 𝑛 in the
     list, the parent is at position 𝑛/2.
     """
     """
     Function Definition: Constructor - Initializes the list and size variable. Note that the list is initialized
     with 0 unline a stack or a queue which also uses list. This is done to ensure that the calculations, n, 2n and 2n+1
     is followed while identifying parent and child nodes.
     """

     def __init__(self):
         self.heap=[0]
         self.size=0

     """
     Property of Min Heap: Top element is the smallest of all elements and parent is smaller than the child.
     Whenever a new element is added, the per_upp function should be executed to ensure data elements follow specific
     rules.
     """
     def per_upp(self,i):

         while i//2>0: #--This ensures that a complete sub tree is present

             if self.heap[i]<self.heap[i//2]:
                 tmp=self.heap[i]
                 self.heap[i]=self.heap[i//2]
                 self.heap[i//2]=tmp
             i=i//2

     """
     Function Definition: Insert element in a heap.
     """

     def insert(self,element):
         self.heap.append(element)
         self.size+=1
         self.per_upp(self.size)

     """
     Function Definition:  In order to maintain the heap order property, all we need to do is swap the root with its smallest
     child less than the root. After the initial swap, we may repeat the swapping process with a node
     and its children until the node is swapped into a position on the tree where it is already less
     than both children. The code for percolating a node down the tree is found in the perc_down
     and min_child methods.
     """

     def perc_down(self,i):

         while (i*2)<=self.size:
             min_data=self.min_child(i)

             if self.heap[i]>self.heap[min_data]:
                 tmp=self.heap[i]
                 self.heap[i]=self.heap[min_data]
                 self.heap[min_data]=tmp

             i=min_data

     def min_child(self,i):
         if (i*2)+1>self.size: #--Checking if the subtree is a part of the tree
             return i*2 #--return index of left child
         else:
             if self.heap[i * 2] < self.heap[i * 2 + 1]: #--check left and right child items
                 return i * 2 #--index of left child
             else:
                 return i * 2 + 1 #--index of right child

     """
     How heap works is, the first element is the minimum and it is deleted and replaced by the one at the bottom.
     Hence once this is done, the heap needs to be restructured to ensure that it adhere to the heap rules.
     """

     def delete(self):
         ret_val = self.heap[1]
         self.heap[1] = self.heap[self.size]
         self.size = self.size - 1
         self.heap.pop()
         self.perc_down(1)
         return ret_val

     def build_heap(self, a_list):
         i = len(a_list) // 2

         self.size = len(a_list)
         self.heap = [0] + a_list[:]

         while (i > 0):
             self.perc_down(i)
             i = i - 1

class Heap:
    """
    Another interesting property of a complete tree is that we can represent it using a single list. We
    do not need to use nodes and references or even lists of lists. Because the tree is complete, the
    left child of a parent (at position 𝑝) is the node that is found in position 2𝑝 in the list. Similarly,
    the right child of the parent is at position 2𝑝 + 1 in the list. To find the parent of any node in
    the tree, we can simply use Python’s integer division. Given that a node is at position 𝑛 in the
    list, the parent is at position 𝑛/2.
    """
    """
    Function Definition: Constructor - Initializes the list and size variable. Note that the list is initialized
    with 0 unline a stack or a queue which also uses list. This is done to ensure that the calculations, n, 2n and 2n+1
    is followed while identifying parent and child nodes. 
    """

    def __init__(self):
        self.heap=[0]
        self.size=0

    """
    Property of Min Heap: Top element is the smallest of all elements and parent is smaller than the child.
    Whenever a new element is added, the per_upp function should be executed to ensure data elements follow specific
    rules.
    """
    def per_upp(self,i):

        while i//2>0: #--This ensures that a complete sub tree is present

            if self.heap[i]>self.heap[i//2]:
                tmp=self.heap[i]
                self.heap[i]=self.heap[i//2]
                self.heap[i//2]=tmp
            i=i//2

    """
    Function Definition: Insert element in a heap. 
    """

    def insert(self,element):
        self.heap.append(element)
        self.size+=1
        self.per_upp(self.size)

    """
    Function Definition:  In order to maintain the heap order property, all we need to do is swap the root with its smallest
    child less than the root. After the initial swap, we may repeat the swapping process with a node
    and its children until the node is swapped into a position on the tree where it is already less
    than both children. The code for percolating a node down the tree is found in the perc_down
    and min_child methods.
    """

    def perc_down(self,i):

        while (i*2)<=self.size:
            max_data=self.max_child(i)

            if self.heap[i]<self.heap[max_data]:
                tmp=self.heap[i]
                self.heap[i]=self.heap[max_data]
                self.heap[max_data]=tmp

            i=max_data

    def max_child(self,i):
        if (i*2)+1>self.size: #--Checking if the subtree is a part of the tree
            return i*2 #--return index of left child
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]: #--check left and right child items
                return i * 2 #--index of left child
            else:
                return i * 2 + 1 #--index of right child

    """
    How heap works is, the first element is the minimum and it is deleted and replaced by the one at the bottom.
    Hence once this is done, the heap needs to be restructured to ensure that it adhere to the heap rules. 
    """

    def delete(self):
        ret_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2

        self.size = len(a_list)
        self.heap = [0] + a_list[:]

        while (i > 0):
            self.perc_down(i)
            i = i - 1


obj=Heap()
obj.build_heap( [5, 3, 1, 9, 7, 8])
print(obj.heap)