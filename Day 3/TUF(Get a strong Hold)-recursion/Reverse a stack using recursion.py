
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if len(s)==0:
            return
        val=s.pop()
        self.Sorted(s)
        self.insert(s,val)
        return s
        
    def insert(self,s=[],val=0):
        if len(s)==0 or val>=s[-1]:
            s.append(val)
            return
        temp=s.pop()
        self.insert(s,val)
        s.append(temp)
        return