from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def __add__(self, autre_boisson):
        if isinstance(autre_boisson, Boisson):
            return BoissonCombinee(self, autre_boisson)
        return NotImplemented

class Cafe(Boisson):
    def cout(self):
        return 18.0

    def description(self):
        return "Café noir"

class The(Boisson):
    def cout(self):
        return 12.0

    def description(self):
        return "Thé vert"

class BoissonCombinee(Boisson):
    def __init__(self, boisson_gauche: Boisson, boisson_droite: Boisson):
        self.gauche = boisson_gauche
        self.droite = boisson_droite

    def cout(self):
        return self.gauche.cout() + self.droite.cout()

    def description(self):
        return f"{self.gauche.description()} mixé avec {self.droite.description()}"

class DecorateurBoisson(Boisson):
    def __init__(self, base_boisson: Boisson):
        self.base_boisson = base_boisson

class Lait(DecorateurBoisson):
    def cout(self):
        return self.base_boisson.cout() + 2.0

    def description(self):
        return self.base_boisson.description() + " au lait"

class Sucre(DecorateurBoisson):
    def cout(self):
        return self.base_boisson.cout() + 1.0

    def description(self):
        return self.base_boisson.description() + " sucré"

class Caramel(DecorateurBoisson):
    def cout(self):
        return self.base_boisson.cout() + 3.0

    def description(self):
        return self.base_boisson.description() + " nappage caramel"

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

class Commande:
    def __init__(self, acheteur):
        self.client = acheteur
        self.panier = []

    def ajouter_boisson(self, item: Boisson):
        self.panier.append(item)

    def calculer_total(self):
        montant = 0
        for item in self.panier:
            montant += item.cout()
        return montant

    def afficher_commande(self):
        print(f"\n=== TICKET DE CAISSE : {self.client.nom} ===")
        for item in self.panier:
            print(f" > {item.description()} : {item.cout()} DH")
        print(f"-----------------------------------")
        print(f"MONTANT TOTAL : {self.calculer_total()} DH")

class CommandeSurPlace(Commande):
    def afficher_commande(self):
        print("[ MODE : CONSOMMATION SUR PLACE ]")
        super().afficher_commande()

class CommandeEmporter(Commande):
    def afficher_commande(self):
        print("[ MODE : À EMPORTER ]")
        frais_emballage = 5.0
        total_avec_frais = self.calculer_total() + frais_emballage
        super().afficher_commande()
        print(f"Total à payer (avec frais d'emballage) : {total_avec_frais} DH")

class Fidelite:
    def ajouter_points(self, acheteur: Client, montant_paye):
        points_gagnes = int(montant_paye)
        acheteur.points_fidelite += points_gagnes
        print(f"*** {points_gagnes} points de fidélité crédités. Nouveau solde : {acheteur.points_fidelite} pts ***\n")

class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        montant_final = self.calculer_total()
        self.ajouter_points(self.client, montant_final)
        print("-> Statut : Commande validée avec succès.")

# --- ZONE DE TESTS ---
mon_client = Client("mehdi abdenbi", 554433, 200)

# On prépare quelques boissons différentes
boisson_1 = Caramel(Sucre(Cafe()))
boisson_2 = Lait(The())
combo_special = Cafe() + The()

# On passe la commande
ma_commande = CommandeFidele(mon_client)
ma_commande.ajouter_boisson(boisson_1)
ma_commande.ajouter_boisson(boisson_2)
ma_commande.ajouter_boisson(combo_special)

# Affichage et validation
ma_commande.afficher_commande()
print("\nValidation en cours...")
ma_commande.valider_commande()