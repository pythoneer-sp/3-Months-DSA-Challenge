class Stack:
    # Create a stack
    def __init__(self):
        self.stack=[]

    # Pushing element in the stack
    def push(self,element):
        self.stack.append(element)

    # If stack is empty
    def isEmpty(self):
        return len(self.stack)==0

    # Deleting an element from the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    # Peek: Returns the top element on the stack.
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    # Returns the size of the stack
    def size(self):
        return len(self.stack)

# Function to sort the stack using recursion  
def sort(s):
    if s.isEmpty(): #Base condition
        return []
    val=s.pop()  # Smaller the input
    sort(s)
    insert(s,val)  # Function to fixed the popped value at original position
    return s

# Helper function to insert the val in the stack
def insert(s,val=0):
    if s.isEmpty() or val>=s.peek():  # Base condition
        s.push(val)
        return
    temp=s.pop()  # Smaller the input
    insert(s,val)
    s.push(temp)
    return

# Creating the stack = 5,1,7,9,4
mystack=Stack()
mystack.push(5)
mystack.push(1)
mystack.push(7)
mystack.push(9)
mystack.push(4)

sort(mystack) # Sort function is called

# Printing the stack
while not mystack.isEmpty():
    print(mystack.pop(), end=" ")