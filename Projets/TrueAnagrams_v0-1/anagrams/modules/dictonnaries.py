from pathlib import Path


ords = list[int]


def str_to_ords(word: str) -> ords:
    ascii_chars: ords = []
    for letter in word:
        ascii_chars.append(ord(letter))
    
    return ascii_chars

def greater_str(a: str, b: str) -> str:
    if ord(a) > ord(b):
        return a
    else:
        return b

def greater_ords(a: ords, b: ords) -> ords:
    for i_a, i_b in zip(a, b):
        if i_a > i_b:
            return i_a
        elif i_b > i_a:
            return i_b
    return i_a


def in_dict(word: str, dictionnary_path: Path) -> bool:
    """
    Search using dichotomy a word.
    Parameters
    ----------
    word : str
        Word to be searched.
    dictionnary_path : Path
        Path of the dict file, sorted in alphabetic order.

    Returns
    -------
    bool
        True if in dict, False otherwise.
    """
    
    
    

if __name__ == "__main__":
    print("# DICTIONNARIES")
    
    import paths
    
    print(greater_ords(str_to_ords("abc"), str_to_ords("aaa")))
    print(greater_ords(str_to_ords("aaa"), str_to_ords("aaa")))
    print(greater_ords(str_to_ords("aaa"), str_to_ords("abc")))
    print(greater_ords(str_to_ords("uui"), str_to_ords("uua")))