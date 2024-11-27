import tkinter as tk
from tkinter import messagebox
from knapsack import Knapsack
import csv  # N'oubliez pas d'importer csv pour charger les objets

class KnapsackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de l'espace dans le camion")

        # Champ pour la capacité du camion
        self.capacity_label = tk.Label(root, text="Capacité du camion (Poids total):")
        self.capacity_label.grid(row=0, column=0)

        self.capacity_entry = tk.Entry(root)
        self.capacity_entry.grid(row=0, column=1)

        # Bouton pour résoudre le problème
        self.solve_button = tk.Button(root, text="Résoudre", command=self.solve)
        self.solve_button.grid(row=2, columnspan=2)

        # Affichage des résultats
        self.result_label = tk.Label(root, text="Résultats:")
        self.result_label.grid(row=3, columnspan=2)

        self.selected_items_label = tk.Label(root, text="Articles sélectionnés:")
        self.selected_items_label.grid(row=4, columnspan=2)

        self.max_value_label = tk.Label(root, text="Valeur maximale:")
        self.max_value_label.grid(row=5, columnspan=2)

        # Initialiser Knapsack (à ce moment, on attend que l'utilisateur remplisse la capacité)
        self.knapsack = None

    def solve(self):
        # Lire la capacité saisie par l'utilisateur
        try:
            capacity = int(self.capacity_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une capacité valide.")
            return

        # Charger les objets si ce n'est pas déjà fait
        if self.knapsack is None:
            self.load_items()

        # Mettre à jour la capacité
        self.knapsack.capacity = capacity

        # Résoudre le problème du sac à dos
        max_value = self.knapsack.solve()
        selected_items = self.knapsack.get_selected_items()

        # Afficher les résultats
        self.max_value_label.config(text=f"Valeur maximale: {max_value}")
        self.selected_items_label.config(text="Articles sélectionnés:")
        
        items_text = "\n".join([f"Poids: {item[0]}, Valeur: {item[1]}" for item in selected_items])
        self.selected_items_label.config(text=f"Articles sélectionnés:\n{items_text}")

    def load_items(self):
        # Charger les objets depuis le fichier CSV
        file_path = "items.csv"  # Chemin vers le fichier CSV
        items = []

        try:
            with open(file_path, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    weight = int(row["poids"])
                    value = int(row["valeur"])
                    items.append((weight, value))

            # Créer l'instance de Knapsack et ajouter les objets
            self.knapsack = Knapsack(0)  # On initialise avec une capacité temporaire
            for weight, value in items:
                self.knapsack.add_item(weight, value)

        except FileNotFoundError:
            messagebox.showerror("Erreur", f"Le fichier {file_path} est introuvable.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement du fichier : {str(e)}")
