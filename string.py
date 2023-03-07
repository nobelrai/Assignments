string = "Python + is + an + awesome + language."
new_string = ""
for i in string:
    if i == "+":
        continue
    new_string = new_string + i
c = new_string.strip("")
print(c)
