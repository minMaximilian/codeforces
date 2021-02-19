x = input()
x = [i for i in x if i != "+"]
x.sort()
x = "+".join(x)
print(x)