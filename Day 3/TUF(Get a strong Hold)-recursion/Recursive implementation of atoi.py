def myAtoi(s):
    if len(s)==0:
        return
    if s[0]==" ":
        s=s[1:]
    if s[0]=="-"or"+":
        print(s[0],end="")
        s=s[1:]
    if s[0].isalpha() is False:
        print(s[0])
        s=s[1:]
    else:
        return
    myAtoi(s)

myAtoi("42")