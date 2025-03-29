# Write a python program to sort an array using recursion

def sort(arr=[]):
    if len(arr)==0: #Base condition
        return []
    val=arr.pop()  # Smaller the input
    sort(arr)
    insert(arr,val)  # Function to fixed the popped value at original position
    return arr

def insert(array=[],val=0):
    if len(array)==0 or val>=array[-1]:  # Base condition
        array.append(val)
        return
    temp=array.pop()  # Smaller the input
    insert(array,val)
    array.append(temp)
    return

print(sort([9,3,2,7,1,5]))