def generateParenthesis( n: int) -> list[str]:
        result=[]
        open_br=n
        close_br=n
        op=""
        def solve(open_br,close_br,op):
            if open_br==0 and close_br==0:
                result.append(op)
                return
            if open_br != 0:
                op1= op + "("
                solve(open_br-1,close_br,op1)
            if close_br>open_br:
                op2= op + ")"
                solve(open_br,close_br-1,op2)
            return
        solve(open_br,close_br,op)
        return result

print(generateParenthesis(3))