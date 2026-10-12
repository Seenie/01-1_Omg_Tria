import random
number = []
def random_number_gen(start, end):
    return random.randint(start, end)

for i in range(10):
    number.append(random_number_gen(1, 10000000000))
    print(f"https://www.roblox.com/users/{number[i]}/profile")







