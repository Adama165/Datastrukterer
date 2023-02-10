class LinkedList:
    
    # The __Node class is used internally by the LinkedList class. It is 
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name). 
    class __Node:
        # Slots is used for memory optimization of the data members.
        # Without slots defined, the data members are inserted in a
        # python dictionary in the class.
        # Defining slots is particularly useful for small classes with 
        # many instances, such as the __Node class
        __slots__ = 'item', 'next'
        def __init__(self,item,next=None):
            self.item = item
            self.next = next
            
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
            
        def setNext(self,next):
            self.next = next
            
    def __init__(self,contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. They both point to a 
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item. 
        # Its purpose is to eliminate special cases in the code below. 
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)
          
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            return cursor.getItem()
        
        raise IndexError("LinkedList index out of range")
    
    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            cursor.setItem(val)
            return 
        
        raise IndexError("LinkedList assignment index out of range")
    
    def insert(self,index,item):
        cursor = self.first
        
        if index < self.numItems: 
            for i in range(index):
                cursor = cursor.getNext()
                
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
            
            
    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                str(type(self)) + " + " + str(type(other)))

        result = LinkedList()
        
        cursor = self.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.first.getNext()
                    
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
   
        return result
    
    
    def __contains__(self,item):
        # TODO: implement __contains__
        if item in self.__iter__():
            return True
        return False
        
    def __delitem__(self,index):
        # TODO: implement __delitem__ 
        delCursor = index
        if index < 0 or index > self.numItems:
            raise IndexError("Index out of range")
        print(self.numItems)
        cursor = self.first
        delCursor = cursor.getNext()
        for i in range(index):
            cursor = delCursor
            delCursor = cursor.getNext()
        print("deletionitem:",delCursor.getItem())
        next = delCursor.getNext()
        cursor.setNext(next)
        if delCursor == self.last:
            self.last = cursor
        self.numItems = self.numItems - 1
            
    def __eq__(self,other):
        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        cursor1 = self.first.getNext()
        cursor2 = other.first.getNext()
        while cursor1 != None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()
            
        return True
    
    def __iter__(self):
        # TODO: implement __iter__.
        for index in range(self.numItems):
            yield self.__getitem__(index)
        #cursor = self.first
        #while cursor:
            #print("loop")
            #yield cursor.getItem()
            #cursor = cursor.getNext()
            
    def __len__(self):
        # TODO: implement __len__.
        length = 0
        for i in self.__iter__():
            length += 1
        return length

    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

        
    def __str__(self):
        retStr = ""
        for item in self:
           retStr += str(item)
           retStr += ", "
        retStr += "\n" 
        return retStr
    
    def __repr__(self):
        retStr = "Linked List: \n"
        retStr += "first: "
        retStr += repr(self.first)
        retStr += "\n"
        retStr += "last: "
        retStr += repr(self.last)
        retStr += "\n"
        retStr += "numItems: "
        retStr += str(self.numItems)
        return retStr
                
""" 
myList = LinkedList()
myList.append(5)
myList.append(6)
myList.append(2)
myList.append(2)
myList.append(4)
myList.append(12)
myList.append(10)
myList.append(3)
myList.append(7)
myList.append(8)
myList.append(9)
myList.append(15) """
#print(myList)
#print(myList.first.getNext())
#print(myList.__getitem__(1))
""" print("loop:")
for i in myList.__iter__():
    print(i)
print("length",myList.__len__())
myList.__delitem__(7)
print(myList) """
#myList.__contains__(5)


        #for i in self.__iter__():
            #if item == i:
                #return True
            #if item != i:
                #return False