from linkedlist_begin import LinkedList

class LinkedQueue:
    def __init__(self):
        """Use a LinkedList to store the queue items"""
        self.items = LinkedList()
                 
    def dequeue(self):
        """TODO: Implement dequeue"""
        if LinkedQueue.isEmpty(self):
            raise RuntimeError("Attempt to dequeue an empty queue")
        
        LinkedList.__delitem__(self,0)
    
    def enqueue(self,item):
        """TODO: Implement enqueue"""
        LinkedList.append(self, item)

        
    def front(self):
        """TODO: Implement front"""
        if LinkedQueue.isEmpty(self):
            raise RuntimeError("Attemt to access front of empty queue")
        
        return self.__getitem__(0)
        
    
    def isEmpty(self):
        """TODO: Implement isEmpty"""
        return len(self) == 0
    
    def clear(self):
        """TODO: Implement clear"""
        self.items = LinkedList()


myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
print(myList)
print("enqueue:",LinkedQueue.enqueue(myList, 5))
print(myList)
print("isempty:",LinkedQueue.isEmpty(myList))
print("front:",LinkedQueue.front(myList))
print("Dequeue:",LinkedQueue.dequeue(myList))
print(myList)
print("clear:",LinkedQueue.clear(myList))
print(myList)
print("isempty:",LinkedQueue.isEmpty(myList))