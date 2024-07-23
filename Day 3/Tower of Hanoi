# Write the program for tower of Hanoi problem

def ToHanoi(n,o,s,f):
  if n==1:
    print("Move disk from " + str(o)+ " to " +str(f))
  else:
    ToHanoi(n-1,o,f,s)
    print("Move disk from " +str(o)+ " to " +str(f))
    ToHanoi(n-1,s,o,f)

ToHanoi(3,"o","s","f")