import sys
from collections import Counter

def count_words(path: str):
    text = open(path, "r", encoding="utf-8").read()
    words = text.lower().split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for key,value in word_dict.items():
        print(key, ": ", value)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <path>") 
        sys.exit(1)
    try:
        count = count_words(sys.argv[1])
    except FileNotFoundError:
        print("File not found.")
