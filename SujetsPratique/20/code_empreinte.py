# Données d'émissions en gCO2e par unité
EMISSIONS: dict[str, int] = {
    'emails_simples': 4,       # par email
    'emails_pj': 19,           # par email avec pièce jointe
    'streaming_sd': 36,        # par heure
    'streaming_hd': 100,       # par heure
    'recherches': 7,           # par recherche
    'stockage_cloud': 10       # par Go par mois
}

# Exemples d'utilisateurs pour les tests
utilisateur1: dict[str, int] = {
    'emails_simples': 150,
    'emails_pj': 20,
    'streaming_sd': 10,
    'streaming_hd': 25,
    'recherches': 500,
    'stockage_cloud': 15
}

utilisateur2: dict[str, int] = {
    'streaming_hd': 15,
    'emails_simples': 100,
    'recherches': 10
}

utilisateur3: dict[str, int] = {
    'emails_simples': 50,
    'emails_pj': 5,
    'streaming_sd': 30,
    'streaming_hd': 5,
    'recherches': 200,
    'stockage_cloud': 5
}

utilisateur4: dict[str, int] = {
    'emails_simples': 100,
    'recherches': 50
}

utilisateur5: dict[str, int] = {
    'emails_simples': 50,
    'recherches': 100
}

utilisateur6: dict[str, int] = {}

utilisateurs: list[dict[str, int]] = [
    utilisateur1,
    utilisateur2,
    utilisateur3,
    utilisateur4,
    utilisateur5,
    utilisateur6,
]

#############################################################################
# Écrire le code de la fonction calculer_empreinte de la question 1         #
#############################################################################
def calculer_empreinte(utilisateur: dict[str, int]) -> int:
    empreinte: int = 0
    for usage, valeur in utilisateur.items():
        empreinte += EMISSIONS[usage] * valeur
    
    return empreinte

#############################################################################
# Écrire le code de la fonction classer_par_impact de la question 2         #
#############################################################################
def classer_par_impact(utilisateur: dict[str, int]) -> dict[str, list[str]]:
    impacts: dict[str, list[str]] = {
        "fort": [],
        "moyen": [],
        "faible": [],
    }

    for usage, valeur in utilisateur.items():
        emission: int = EMISSIONS[usage] * valeur
        if 1000 <= emission:
            impacts["fort"].append(usage)
        elif 200 <= emission < 1000:
            impacts["moyen"].append(usage)
        else:
            impacts["faible"].append(usage) 
    
    return impacts


#############################################################################
# Fonction fournie pour la question 3                                       #
#############################################################################

def comparer(
    u1: dict[str, int], 
    u2: dict[str, int]
) -> dict[str, int]:
    """
    Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, la différence des
    émissions (émissions de l'utilisateur 2 moins celles de l'utilisateur 1).
    Si une activité est absente chez un utilisateur, on considère que
    son émission vaut 0.
    """
    differences: dict[str, int] = {}
    
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1: int = u1[activite]
        if activite in u2:
            quantite2: int = u2[activite]
        
        emission1: int = quantite1 * EMISSIONS[activite]
        emission2: int = quantite2 * EMISSIONS[activite]
        differences[activite] = emission2 - emission1
    return differences


def test_comparer():
    difference_4_5: dict[str, int] = comparer(utilisateur4, utilisateur5)
    assert difference_4_5['emails_simples'] == -200  # (50-100) * 4
    assert difference_4_5['recherches'] == 350     # (100-50) * 7
    
    difference_1_6: dict[str, int] = comparer(utilisateur1, utilisateur6)
    for usage, valeur in difference_1_6.items():
        assert valeur < 0

    print("Test: comparer - Passé.")
    return


#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################
def comparer_v2(u1: dict[str, int], u2: dict[str, int]) -> dict[str, float]:
    """
    Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, l'écart des émissions
    sous forme de pourcentage, en proportion de la première émission.
    """
    ecarts: dict[str, float] = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1: int = u1[activite]
        if activite in u2:
            quantite2: int = u2[activite]
        
        emission1: int = quantite1 * EMISSIONS[activite]
        emission2: int = quantite2 * EMISSIONS[activite]

        ecarts[activite] = ((emission2 - emission1) / emission1 * 100
            if emission1 != 0
            else +float("inf")                   
        )
    return ecarts

def main() -> None:
    print("\nQuestion 1.")
    assert calculer_empreinte(utilisateur1) == 7490
    for index, utilisateur in enumerate(utilisateurs, 1):
        print(f"{index}: {calculer_empreinte(utilisateur)}")


    print("\nQuestion 2.")
    for index, utilisateur in enumerate(utilisateurs, 1):
        print(f"{index}: {classer_par_impact(utilisateur)}")


    print("\nQuestion 3.")
    test_comparer()

    print("\nQuestion 4.")
    comparer_v2(utilisateur1, utilisateur2)
    comparer_v2(utilisateur6, utilisateur1)
    
    for index1, u1 in enumerate(utilisateurs, 1):
        for index2, u2 in enumerate(utilisateurs, 1):
            print(f"{index1};{index2}: {comparer_v2(u1, u2)}")


if __name__ == "__main__":
    main()
