
def countGoodNumbers(n: int) -> int:
    MOD = 10**9+7
    def pow(x,n): # Function to return power of x
        
        if n==0:
            return 1
        if n%2==0:
            half = pow(x,n//2)
            return (half*half) % MOD
        else:
            return (x*pow(x,n-1)) % MOD
    return (pow(5,(n+1)//2)*pow(4,n//2)) % MOD