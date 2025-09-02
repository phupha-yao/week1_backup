def is_prime(n: int):
    if n < 2:
        return False
    for x in range(2, int(pow(n,0.5) + 1)):
        if n % x == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(6))