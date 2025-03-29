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
    
    
def deleteMid(s,stacksize):
    if stacksize==0:
        return s
    k=stacksize//2 +1
    solve(s,k)
    return s

def solve(s,k=0):
    if k==1:
        s.pop()
        return s
    val=s.pop()
    solve(s,k-1)
    s.push(val)
    return s

# Creating the stack = 5,1,7,9,4
mystack=Stack()
mystack.push(5)
mystack.push(1)
mystack.push(7)
mystack.push(9)
mystack.push(4)

deleteMid(mystack,5)
# Printing the stack
while not mystack.isEmpty():
    print(mystack.pop(), end=" ")