def generate_strings(n):
    if n == 1:
        return ["0", "1"]
    
    smaller_strings = generate_strings(n - 1)
    result = []
    
    for s in smaller_strings:
        if s[-1] == "0":
            result.append(s + "0")
            result.append(s + "1")
        else:
            result.append(s + "0")
    
    return result

# Example usage
n = 4
print(generate_strings(n))
