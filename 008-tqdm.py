"""
Progress bar into the console with tqdm

link: https://github.com/tqdm/tqdm
"""
from time import sleep
from tqdm import tqdm

# First method
for i in tqdm(range(20)):
    sleep(0.1)
    
# Second method
progressbar = tqdm(total=20)
for i in range(20):
    sleep(0.1)
    progressbar.update(1)
progressbar.close()

