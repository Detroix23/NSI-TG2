# Documentation du module doctest :
# https://docs.python.org/3/library/doctest.html (en anglais)
# https://docs.python.org/fr/3/library/doctest.html (en français)

import doctest

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


def est_parfait(n) : 
   '''n est un entier strictement positif
   parfait(n) vaut True si l'entier n est parfait ou False sinon.
   Un nombre parfait est tel que la somme de ses diviseurs est égale à son double.
   >>> est_parfait(2)
   False
   >>> est_parfait(6)
   True
   >>> est_parfait(27)
   False
   >>> est_parfait(28)
   True'''

   assert(n > 0 and type(n) == int), "l'argument doit être un entier strictement positif"
   diviseurs = [i for i in range(1, n + 1) if n % i  == 0]
   return sum(diviseurs) == 2 * n

# ---------------- Programme principal -------------------- #

doctest.testmod()
# Si aucun message d'erreur ne s'affiche, alors tous les tests sont passés.   

# Pour obtenir un résumé détaillé de ce qui a été fait, on ajoute un paramètre. 
# Décommenter la ligne suivante pour tester. 

# doctest.testmod(verbose = True)

