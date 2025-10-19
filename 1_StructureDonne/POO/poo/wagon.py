class Train:
    def __init__(self):
        "Constructeur"
        self.premier = None
        self.nb_wagons = 0

    def est_vide(self):
        """renvoie True si ce train est vide (ne comporte aucun wagon),
        False sinon
        """
        return self.nb_wagons == 0

    def donne_nb_wagons(self):
        "Renvoie le nombre de wagons de ce train"
        return self.nb_wagon

    def transporte_du(self, contenu):
        """Détermine si ce train transporte du {contenu} (une chaine de caractères).
        Renvoie True si c'est le cas, False sinon
        """
        wagon = self.premier
        while wagon is not None:
            if wagon.contenu == contenu:
                return True
            wagon = wagon.suivant
        return False

    def ajoute_wagon(self, nouveau):
        """Ajoute un wagon à la fin de ce train.
        L'argument est le wagon à ajouter
        """
        if self.est_vide():
            self.premier = nouveau
        else:
            wagon = self.premier
            while self.suivant is not None:
                wagon = self.suivant
            wagon.suivant = nouveau
        self.nb_wagons += 1 

    def supprime_wagon_de(self, contenu):
        """Supprime le premier wagon de {contenu}
        Renvoie False si ce train ne contient pas de {contenu},
        True si la suppression est effectuée
        """
        # On parcourt le train afin de trouver le contenu
        precedent = None
        wagon = self.premier
        while wagon is not None and wagon.contenu != contenu:
            precedent = wagon
            wagon = wagon.suivant

        if wagon is None:  # on a parcouru tout le train sans trouver le contenu
            return False
        if precedent is None:  # le wagon supprimé est le premier du train
            self.premier = wagon....
        else:  # le wagon supprimé n'est pas le premier
            precedent.... = wagon....
        self.nb_wagons -= ...
        return ...

    def __repr__(self):
        "Affichage dans la console"
        contenus_wagons = ['']
        wagon = self.premier
        while wagon is not None:
            contenus_wagons.append(str(wagon))
            wagon = wagon.suivant
        return "Locomotive" + " - ".join(contenus_wagons)

    def __str__(self):
        "Conversion en string"
        return self.__repr__()

# Tests

train = Train()
w1 = Wagon("blé")
train.ajoute_wagon(w1)
w2 = Wagon("riz")
train.ajoute_wagon(w2)
train.ajoute_wagon(Wagon("sable"))
assert str(train) == 'Locomotive - Wagon de blé - Wagon de riz - Wagon de sable'
assert train.est_vide() is False
assert train.donne_nb_wagons() == 3
assert train.transporte_du('blé') is True
assert train.transporte_du('matériel') is False
assert train.supprime_wagon_de('riz') is True
assert str(train) == 'Locomotive - Wagon de blé - Wagon de sable'
assert train.supprime_wagon_de('riz') is False
