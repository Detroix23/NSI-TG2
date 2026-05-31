
import pprint
from typing import Union, Literal

import ascii

#############################################################################
# Question 1 et 2 : Écrire les codes des fonctions bin2dec et qrcode2dec
#              Proposer un test de qrcode2dec
#############################################################################

def bin2dec(binary_tuple: tuple[Union[Literal[1], Literal[0]], ...]) -> int:
    """
    Calcule le nombre décimal depuis un tuple de bits.
    """
    decimal: int = 0
    index: int = 0
    while index < len(binary_tuple):
        decimal += binary_tuple[len(binary_tuple) - index - 1] * 2 ** index 
        index += 1

    return decimal


def qrcode2dec(
    qr_code: list[tuple[Union[Literal[1], Literal[0]], ...]]
) -> list[int]:
    return [bin2dec(line) for line in qr_code]

def tests_qrcode2dec_1() -> None:
    # implémentation du QR Code de la figure 1:
    qrcode_fig1 = ascii.figure1
    
    assert qrcode2dec(qrcode_fig1) == [77, 46, 72, 97, 114, 97]


#############################################################################
# Question 3 : Fonctions dec2str et test_dec2str
#############################################################################
def dec2str(liste_dec: list[int]):
    """ entrée: liste d'entiers décimaux
        sortie: chaine de caractère formée des caractères correspondant
        de la table ascii """
    UNKNOWN: str = "?"
    table_ascii: dict[int, str] = ascii.dict_ascii
    chaine: str = ""

    for entier in liste_dec:
        # Correction: vérifier si `entier` dans la table, sinon mettre `?`.
        chaine += (table_ascii[entier]
            if entier in table_ascii
            else UNKNOWN
        )
    return chaine


def test_dec2str():
    """ Teste la fonction dec2str avec des données issues du module fourni """
    tests = [ascii.test1, ascii.test2, ascii.test3]
    for test in tests:
        print(dec2str(test))


def qrcode2str(qrcode):
    return dec2str(qrcode2dec(qrcode))

#############################################################################
# Question 4 : Fonction str2qrcode déficiente
#############################################################################


def adjust_left(target: str, length: int, adjust: str = "0") -> str:
    add: int = max(0, length - len(target))
    return adjust * add + target

def str2qrcode(message: str) -> list[int]:
    """
    Convertit une chaine de caractères en liste de tuples binaires.
    """
    qrcode = []
    table_inverse: dict[str, int] = {
        valeur: cle 
        for cle, valeur in ascii.dict_ascii.items()
    }

    for caractere in message:
        entier: int = table_inverse.get(caractere, 63)
        # Source du problème: pas de zero à la fin.
        binaire_str: str = adjust_left(bin(entier)[2:], 8)
    
        ligne: tuple[int, ...] = tuple(int(bit) for bit in binaire_str)
        qrcode.append(ligne)
    
    return qrcode


def main() -> None:
    # Question 1.
    print("Question 1.")

    code1: list[tuple[Union[Literal[1], Literal[0]], ...]] = [
        (0, 1, 0, 0, 1, 1, 0, 1), 
        (0, 0, 1, 0, 1, 1, 1, 0),
        (0, 1, 0, 0, 1, 0, 0, 0),
        (0, 1, 1, 0, 0, 0, 0, 1),
        (0, 1, 1, 1, 0, 0, 1, 0),
        (0, 1, 1, 0, 0, 0, 0, 1),
    ]

    print("Nom: `M. Hara`")
    for code in ascii.figure1:
        print(f"`{ascii.dict_ascii[(bin2dec(code))]}`", end=" ")

    # Question 2.
    print("Question 2.")

    tests_qrcode2dec_1()
    print("Passé.")

    # Question 3.
    print("Question 3.")
    
    test_dec2str()

    # Question 4.
    print("Question 4.")

    pprint.pprint(str2qrcode("M.Hara"))

if __name__ == "__main__":
    main()
