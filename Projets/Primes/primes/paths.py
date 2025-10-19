"""
PRIMES
paths.py
Paths variable across the program.
"""

import pathlib

# Prime numbers known files directory.
INT: pathlib.Path = pathlib.Path("../data/int")




if __name__ == "__main__":
    import os
    
    print("# Primes")
    print("## PATHS")
    
    assert os.path.isdir(INT)
    