import os
import random

os.mkdir("a")
directory_path = os.getcwd() + r"\a"
for i in range(1, 21):
    open(os.path.join(directory_path, f"{i}.txt"), "w")
count = len(os.listdir(directory_path))
print(count)
for i in range(11):
    z = random.randint(1, 21)
    if os.path.exists(directory_path + f"\{i}.txt"):
        os.remove(directory_path + f"\{i}.txt")
count = len(os.listdir(directory_path))
print(count)
