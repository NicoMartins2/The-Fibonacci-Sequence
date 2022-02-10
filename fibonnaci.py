# Fibonnaci Sequence
import time

def fibonnaci():
    x, y = 1, 1
    while 1:
        time.sleep(1)
        z = x + y
        print(f"{x} + {y} = {z} ")
        print()
        x = y
        y = z
        
fibonnaci()