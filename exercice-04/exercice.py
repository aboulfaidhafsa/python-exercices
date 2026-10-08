ventes = [
    {"produit": "cafe", "quantite": 120, "prix": 2.5},
    {"produit": "the", "quantite": 80, "prix": 2.0},
    {"produit": "jus", "quantite": 45, "prix": 3.5},
]
ca_par_produit = {vente["produit"]: vente["quantite"] * vente["prix"] for vente in ventes}
print(f"Ca par produit ; {ca_par_produit}")
ca_total = sum(ca_par_produit.values())
print(f"Ca chiffre d'affaires total ; {ca_total}")
print(f"Produit le plus vendu ; {max(ca_par_produit, key=ca_par_produit.get)}")
