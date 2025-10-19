"""
PRIMES
saves.py
Save and read .prime files
"""

import paths


def save_list(primes: list[int], file_name: str = "main") -> int:
    """
    Save a list of int in a file, one per line.
    Return 0 if no problem happened, 1 after an OSError.
    """
    exit_code: int = 0
    try:
        with open(paths.INT / (file_name + ".prime"), 'w') as save:
            for prime in primes:
                save.write(str(prime) + "\n")
            
    except OSError as exception:
        print(f"(!) - Os error saving {file_name}: {exception}.")
        exit_code = 1
        
    return exit_code


def read(file_name: str = "main", raise_type: bool = True) -> list[int]:
    """
    Read a .prime file, and returns a list of int.
    """
    primes: list[int] = list()
    try:
        with open(paths.INT / (file_name + ".prime"), 'r') as save:
            for line in save:
                if not line:
                    pass
                elif line[0] == "#":
                    pass
                else:
                    try:
                        primes.append(int(str(line)))
                    except TypeError:
                        if raise_type:
                            raise TypeError(f"(X) - Line is not a number {line}.")
                        else:
                            print(f"(!) - Line is not a number {line}.")
                        
    except OSError as exception:
        print(f"(!) - Os error reading {file_name}: {exception}.")
    
    return primes


if __name__ == "__main__":
    primes: list[int] = [49919, 49921, 49927, 49937, 49939, 49943, 49957, 49991, 49993, 49999]
    
    # print(save_list(primes))
    print(read("main"))