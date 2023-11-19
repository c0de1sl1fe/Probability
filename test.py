import matplotlib
from tqdm import tqdm
import time

with tqdm(100, desc="Gen") as pbar:
    for i in range(0, 10):
        time.sleep(1)
        pbar.update(10)
