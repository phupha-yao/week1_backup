def list_comp(n: list):
    sum = 0
    for i in n:
        if i**0.5 % 2 == 0:
            sum = sum + 1
    return sum

if __name__ == "__main__":
    print(list_comp([4,4,5,16,9,144,169]))