year = input()
test = year
test = int(test) + 1
test = str(test)

def uniqueYear(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return True
    
    return False

while uniqueYear(test):
    test = int(test) + 1
    test = str(test)

print(test)

