"""
Projet 2 - Test SARAA : Héritage
Thème : gestion simple d'employés dans une entreprise.
"""


class Employe:
    """Classe de base : un employé générique."""

    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self):
        return self.salaire_base

    def presenter(self):
        return f"{self.nom} - salaire : {self.calculer_salaire()} €"


class Developpeur(Employe):
    """Hérite d'Employe, ajoute une prime liée au langage maîtrisé."""

    def __init__(self, nom, salaire_base, langage_principal):
        super().__init__(nom, salaire_base)
        self.langage_principal = langage_principal

    def calculer_salaire(self):
        prime = 200
        return self.salaire_base + prime

    def presenter(self):
        base = super().presenter()
        return f"{base} (Développeur {self.langage_principal})"


class Manager(Employe):
    """Hérite d'Employe, gère une équipe et touche une prime de gestion."""

    def __init__(self, nom, salaire_base, taille_equipe):
        super().__init__(nom, salaire_base)
        self.taille_equipe = taille_equipe

    def calculer_salaire(self):
        prime = 50 * self.taille_equipe
        return self.salaire_base + prime

    def presenter(self):
        base = super().presenter()
        return f"{base} (Manager, équipe de {self.taille_equipe})"


def demonstration():
    equipe = [
        Employe("Alice", 2000),
        Developpeur("Bilal", 2200, "Python"),
        Manager("Chloé", 2500, 4),
    ]

    for employe in equipe:
        print(employe.presenter())

    # Vérification : Developpeur et Manager sont bien des Employe (héritage)
    for employe in equipe:
        print(f"{employe.nom} est un Employe :", isinstance(employe, Employe))


if __name__ == "__main__":
    demonstration()
