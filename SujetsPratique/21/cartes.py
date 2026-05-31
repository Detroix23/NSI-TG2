
import datetime

# Variable contenant les délais en jours pour chaque niveau (index 0 à 4)
DELAIS: list[int] = [1, 3, 7, 15, 30]

def date_future(nb_jours: int) -> datetime.date:
    """Renvoie la date située nb_jours après aujourd'hui"""
    return datetime.date.today() + datetime.timedelta(days=nb_jours)

class Carte:
    question: str
    reponse: str
    niveau: int
    date_prochaine: datetime.date

    def __init__(self, question: str, reponse: str) -> None:
        self.question = question
        self.reponse = reponse
        self.niveau = 0
        # À la création, la carte est à réviser le jour même
        self.date_prochaine = datetime.date.today()

    def __repr__(self) -> str:
        return f"<Carte: {self.question} (Niveau {self.niveau})>"

    #############################################################################
    # Écrire la méthode traiter_reponse(self, succes) de la question 1          #
    #############################################################################

    def traiter_reponse(self, succes: bool) -> None:
        if succes:
            self.niveau = min(4, self.niveau + 1)
        else:
            self.niveau = 0
        
        self.date_prochaine = date_future(DELAIS[self.niveau])
        

#############################################################################
# Écrire la fonction extraire_cartes_du_jour de la question 2               #
#############################################################################
def extraire_cartes_du_jour(
    paquet: list[Carte], 
    date_jour: datetime.date
) -> list[Carte]:
    return [
        carte
        for carte in paquet
        if carte.date_prochaine <= date_jour
    ]

#############################################################################
# Fonction défaillante à analyser et corriger pour la question 3            #
#############################################################################

def extraire_cartes_a_renforcer(paquet: list[Carte]) -> list[Carte]:
    """
    Parcourt le paquet et renvoie la liste des cartes ayant le 
    niveau d'avancement le plus faible.
    """
    if len(paquet) == 0:
        return []

    niveau_min: int = paquet[0].niveau

    # Correction de la faille: il faut faire:
    # - une boucle pour le minimum;
    # - une autre pour ajouter les cartes.

    for carte in paquet:
        if carte.niveau < niveau_min:
            niveau_min = carte.niveau

    return [
        carte
        for carte in paquet
        if carte.niveau <= niveau_min
    ]


def test_renforcement():
    # Création d'un paquet de test
    c1 = Carte("Capitale de l'Italie ?", "Rome")
    c1.niveau = 2

    c2 = Carte("7 x 8 ?", "56")
    c2.niveau = 1

    c3 = Carte("Symbole du Fer ?", "Fe")
    c3.niveau = 2

    mon_paquet = [c1, c2, c3]

    # Appel de la fonction défaillante
    resultat = extraire_cartes_a_renforcer(mon_paquet)

    print("Cartes à renforcer (celles ayant le niveau le plus bas) :")
    print(resultat)

def main() -> None:
    # Des cartes et un paquet de cartes pour réaliser des tests
    c1 = Carte("Capitale de l'Italie ?", "Rome")
    c1.niveau = 2
    c1.date_prochaine = date_future(4)
    c2 = Carte("7 x 8 ?", "56")
    c2.date_prochaine = date_future(1)
    c3 = Carte("Symbole du Fer ?", "Fe")
    c3.date_prochaine = date_future(7)

    paquet: list[Carte] = [c1, c2, c3]

    # Question 1.
    print("Question 1.")
    c1.traiter_reponse(True)
    c3.traiter_reponse(False)

    # Question 2.
    print("Question 2.")
    print(paquet)
    print(extraire_cartes_du_jour(paquet, date_future(1)))

    # Question 3.
    print("Question 3.")
    print(extraire_cartes_a_renforcer(paquet))


if __name__ == "__main__":
    main()
