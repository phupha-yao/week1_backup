print("Enter a string: ", end="")
user_input = input()
charCount = {}
#counting characters and storing in a dictionary
for i in user_input:
    if i in charCount:
        charCount[i] = charCount[i] + 1
    else:
        charCount[i] = 1

#outputing the dicitonary
for key,value in charCount.items():
    print(key, ":", value)
