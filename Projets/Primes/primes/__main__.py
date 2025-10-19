"""
PRIMES
__main__.py
Try to find prime numbers efficently
"""
import time
from typing import Callable

import saves

def check_naive(n: int) -> bool:
    """
    "Naive way". Check every number from 2 to n, and check the modulo.
    Still includes starting from 2, going to half of the number, steping 
    2 number each time.
    """
    iterator: int = 3
    # Init with modulo of 2, to remove all multiple of 2 modulos.
    is_prime: bool = n % 2 != 0
    while iterator < ((n // 2) + 1) and is_prime:
        is_prime = (n % iterator != 0)
        
        iterator += 2
        
    return is_prime


def check(n: int) -> bool:
    """
    Alias for the current best accepted primality checker.
    """
    time_elapsed: float = time.monotonic()
    primality: bool = check_naive(n)
    time_elapsed =  time.monotonic() - time_elapsed
    return PrimeResult(
        n, 
        primality,
        time_elapsed
    )


def search_only_primes(limit: int, file_name: str = "") -> set[int]:
    """
    Search all the primes, and return a set of int.
    Each modulo are only prime numbers. 
    Because if the number is not dividable by n in N, it cannot be divided by
    n * k, for any k in N.
    Check each numbers from 3, or need a save file for already found prime numbers.
    """
    known: list[int] = []
    current: int = 3
    time_elapsed: float = time.monotonic()
    
    if file_name:
        known = saves.read(file_name, raise_type=True)
    if not known:
        known = [2, 3]
    else:
        current = known[-1] + 2

        
    
    while current <= limit:
        is_prime: bool = True
        iterator_known: int = 0
        tester: int = 2
        mid: int = current // 2 + 1
        in_known: bool = True
        
        while in_known and is_prime and tester < mid:
            is_prime = current % tester != 0
            
            iterator_known += 1
            tester = known[iterator_known]
            
            in_known = iterator_known <= len(known) - 1
            
        while not in_known and is_prime and tester < mid:
            is_prime = current % tester != 0
            
            tester += 2
        
        if is_prime:
            known.append(current)
        
        current += 2
    
    time_elapsed = time.monotonic() - time_elapsed
    
    if file_name:
        saves.save_list(known, file_name)
    
    return TestResult(time_elapsed, limit, 0, set(known))
    

class PrimeResult:
    number: int
    prime: bool
    time_elapsed: float
    
    def __init__(self, number: int, prime: bool, time_elapsed: float) -> None:
        self.number = number
        self.prime = prime
        self.time_elapsed = time_elapsed
    
    def __str__(self) -> None:
        return f"PrimeResult: {self.number}, prime: {self.prime}, time: {self.time_elapsed:.2f}"
    

class TestResult:
    time_elapsed: float
    upper_limit: int
    lower_limit: int
    results: set[int]
    
    def __init__(
        self, 
        time_elapsed: float, 
        upper_limit: int, 
        lower_limit: int = 0, 
        results: set[int] = set()
    ) -> None:
        self.time_elapsed: float = time_elapsed
        self.upper_limit: int = upper_limit
        self.lower_limit: int = lower_limit
        self.results: set[int] = results

    def __str__(self) -> str:
        return f"""TestResults:
    - Time: {self.time_elapsed:.2f}s
    - Limits: {self.lower_limit}, {self.upper_limit}
    - Results: {list(self.results)[-20:]}
"""


def test(limit: int, function: Callable[int, bool]) -> TestResult:
    """
    Test a primality function.
    """
    run_time: float = time.monotonic()
    results: set[int] = set() 
    for n in range(0, limit):
        if function(n):
            results.add(n)
    run_time = time.monotonic() - run_time
    
    return TestResult(run_time, limit, 0, results)
    

def main() -> None:
    n1 = check(400001)
    print("n1:", n1)
    
    print(search_only_primes(250000, "main"))
    
    """
    maximum = 500000
    for i in range(100000, maximum, 100000):
        print(search_only_primes(i))
    """
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    