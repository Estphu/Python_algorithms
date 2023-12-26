import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s - %(message)s',
)

cakes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

num_choices = 1000

counts = {cake: 0 for cake in cakes}

for i in range(num_choices):
    chosen_cake = random.choice(cakes)
    counts[chosen_cake] += 1

    logging.info(f'J Bakers Chose: {chosen_cake}')

for cake, count in counts.items():
    if count == max(counts.values()):
        print(f'Congragulation!!! {cake} was selected: {count} times')
    else:
        print(f'{cake} was selected: {count} times')