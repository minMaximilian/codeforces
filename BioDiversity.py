x = int(input())
z = []
for _ in range(x):
    z += [input()]
meme = {i: z.count(i) for i in z}