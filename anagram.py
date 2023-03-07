a = input("Enter a word = ")
b = input("Enter another word = ")
c = sorted(a)
d = sorted(b)
if c == d:
    print("Its anagram")
else:
    print("It's not an anagram")
