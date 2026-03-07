class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print("Matricule:", self.matricule)
        print("Marque:", self.marque)
        print("Couleur:", self.couleur)

class Parc:
    def __init__(self, ID, adresse, capacite):
        self.ID = ID
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoiture = []

