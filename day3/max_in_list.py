def max_in_list(n: list):
    max = n[0]
    for i in range(1, len(n)):
        if n[i] > max:
            max = n[i]
    return max

if __name__ == "__main__":
    print(max_in_list([-1, -5, -4]))
