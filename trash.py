from random import randint
with open("random_10k_+-100000.txt", "w") as f:
    for i in range(10000):
        f.write(str(randint(-100000, 100000)) + "\n")