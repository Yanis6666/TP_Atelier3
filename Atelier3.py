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

    def entrerVoiture(self, voiture):

        if len(self.listeVoitures) >= self.capacite:
            print("Parc est plein")
            return

        for n in self.listeVoitures:
            if n.matricule == voiture.matricule:
                print("Voiture est deja dans le parc")
                return

        self.listeVoitures.append(voiture)
        print("Voiture est ajoutée au parc")

    def sortirVoiture(self, voiture):

        if voiture in self.listeVoitures:
            self.listeVoitures.remove(voiture)
            print("Voiture sortie du parc")
        else:
            print("Voiture non presente dans le parc")