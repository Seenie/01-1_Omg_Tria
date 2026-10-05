import random

speed = []
year = []

def random_number_gen(start, end):
    return random.randint(start, end)

for i in range(10):
    speed.append(random_number_gen(50, 100))

for i in range(10):
    year.append(random_number_gen(2000, 2023))


