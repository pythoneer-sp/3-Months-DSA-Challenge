# Write a program in python to reverse an array using recursion

def reverse(arr=[]):
  if len(arr)==0:
    return []
  last_element=arr.pop()
  return [last_element]+reverse(arr)

print(reverse([1,2,3,4,5,6]))