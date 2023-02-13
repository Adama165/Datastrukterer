from linkedlist_begin import LinkedList

class LinkedStack:
    def __init__(self):
        """Use a LinkedList to store the stack items"""
        self.items = LinkedList()
                 
    def pop(self):
        """TODO: Implement pop"""
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")
        delitem = self.items.__getitem__(self.items.numItems - 1)
        self.items.__delitem__(self.items.numItems - 1)
        return delitem

    def push(self,item):
        """TODO: Implement push"""
        self.items.append(item)
        
    def top(self):
        """TODO: Implement top"""
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")

        return self.items.last.getItem()

    def isEmpty(self):
        """TODO: Implement isEmpty"""
        return self.items.numItems == 0

    def clear(self):
        """TODO: Implement clear"""
        self.items = LinkedList()

""" myStack = LinkedStack()
print(LinkedStack.isEmpty(myStack))
print(LinkedStack.push(myStack,3))
print(LinkedStack.push(myStack,5))
print(LinkedStack.push(myStack,6))
print(LinkedStack.push(myStack,8))
print(myStack)
print(LinkedStack.isEmpty(myStack))
print(LinkedStack.pop(myStack))
print(LinkedStack.top(myStack)) """