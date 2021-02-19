sequence = [input() for i in range(int(input()))]
print((sequence.count("X++") + sequence.count("++X"))-(sequence.count("X--") + sequence.count("--X")))