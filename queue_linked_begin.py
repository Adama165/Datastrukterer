from linkedlist_begin import LinkedList

class LinkedQueue:
    def __init__(self):
        """Use a LinkedList to store the queue items"""
        self.items = LinkedList()
                 
    def dequeue(self):
        """TODO: Implement dequeue"""
        #if LinkedQueue.isEmpty(self):
            #raise RuntimeError("Attempt to dequeue an empty queue")
        delitem = self.items.__getitem__(0)
        self.items.__delitem__(0)
        return delitem
    
    def enqueue(self,item):
        """TODO: Implement enqueue"""
        self.items.append(item)
        
    def front(self):
        """TODO: Implement front"""
        return self.items.first.getNext().getItem()
    
    def isEmpty(self):
        """TODO: Implement isEmpty"""
        return self.items.first.getNext() is None

    def clear(self):
        """TODO: Implement clear"""
        self.items = LinkedList()



""" myQueue = LinkedQueue()
myQueue.enqueue(3)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue)
print(LinkedQueue.isEmpty(myQueue))
print(LinkedQueue.front(myQueue)) """
""" print("enqueue:",LinkedQueue.enqueue(myList, 5))
print(myList)
print("isempty:",LinkedQueue.isEmpty(myList))
print("front:",LinkedQueue.front(myList))
print("Dequeue:",LinkedQueue.dequeue(myList))
print(myList)
print("clear:",LinkedQueue.clear(myList))
print(myList)
print("isempty:",LinkedQueue.isEmpty(myList)) """