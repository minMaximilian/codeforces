x = input().lower()
vowels = "aeiouy"
newstr = ([i for i in x if i not in vowels])
j = 0
while j != len(newstr):
    newstr.insert(j, ".")
    j += 2

print("".join(newstr))