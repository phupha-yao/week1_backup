def factorial(n: int):
    if n == 1:
        return 1
    
    return factorial(n - 1) * n

if __name__ == "__main__":
    print(factorial(6))