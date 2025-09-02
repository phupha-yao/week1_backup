print("Please input a list of numbers, separated by spaces:")
user_input = input()
numbers = user_input.split()
average = 0
for x in range(0, len(numbers)):
    average = average + float(numbers[x])
average = average / len(numbers)
print("The average is:", average)