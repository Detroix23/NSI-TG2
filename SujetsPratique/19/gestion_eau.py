"""
# Programme de contrôle des réservoirs.
gestion_eau.py
"""

from donnees import Reservoir, reservoirs, reservoirs_test1 

# Question 1 : écrire la fonction est_en_penurie
def est_en_penurie(reservoirs: list[Reservoir], nom: str) -> bool:
    reservoir: Reservoir = reservoirs[0]
    for disponible in reservoirs:
        if disponible["nom"] == nom:
            reservoir = disponible
    
    return reservoir["volume"] / reservoir["capacite"] < 0.20
    
# Question 2 : écrire la fonction volume_par_district
def volume_par_district(reservoirs: list[Reservoir]) -> dict[str, int]:
    volumes: dict[str, int] = {}

    for reservoir in reservoirs:
        district: str = str(reservoir["district"])
        if district in volumes:
            volumes[district] += reservoir["volume"]
        else:
            volumes[district] = reservoir["volume"]

    return volumes

# Question 3
def volume_moyen(reservoirs: list[Reservoir]) -> float:
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    somme_totale: int = 0

    for r in reservoirs:
        somme_totale += r["volume"]

    moyenne: float = somme_totale / len(reservoirs)

    return moyenne

def test_volume_moyen() -> None:
    moyenne1: float = volume_moyen(reservoirs)

    assert len(reservoirs) > 0
    
    maximum_volume: int = 0
    for reservoir in reservoirs:
        if reservoir["volume"] > maximum_volume:
            maximum_volume = reservoir["volume"]
    assert moyenne1 < maximum_volume


    assert volume_moyen(reservoirs_test1) == (55000 + 45000) / 2


# Question 4
def liste_districts(reservoirs) -> list[str]:
    """
    Renvoie la liste des districts présents dans les données.
    """
    liste: list[str] = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(
    reservoirs: list[Reservoir]
) -> dict[str, list[Reservoir]]:
    """
    Renvoie un dictionnaire associant chaque district à la liste
    des réservoirs qui s'y trouvent.
    """
    liste_rpd: dict[str, list[Reservoir]] = {}
    for r in reservoirs:
        district: str = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        
        liste_rpd[district].append(r)
    return liste_rpd


def districts_vulnerables(reservoirs) -> list[str]:
    print("Districts vulnerables.")
    moyenne: float = volume_moyen(reservoirs)
    print(f"Moyenne: {moyenne}")

    vulnerables: list[str] = []

    for district in liste_districts(reservoirs):
        moyenne_district: float = volume_moyen(
            reservoirs_par_district(reservoirs)[district]
        )

        ecart: float = 1.0 - ((moyenne_district - moyenne) / moyenne)
        print(f"{district=}: {moyenne_district=}, ecart={ecart:.2f}")


        if ecart < 0.80:
            vulnerables.append(district)

    return vulnerables


def main() -> None:
    print("\nQuestion 1.")

    print("\nQuestion 2.")
    print(volume_par_district(reservoirs))

    print("\nQuestion 3.")
    test_volume_moyen()

    print("\nQuestion 4.")
    print(districts_vulnerables(reservoirs))

if __name__ == "__main__":
    main()
