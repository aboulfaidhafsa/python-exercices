produit="Clavier"
prix_ht=19.90
tva=0.20
prix_ttc=prix_ht*(1+tva)
quantite = 3
total = quantite * prix_ttc
print(f"Total à payer pour {quantite} {produit}(s): {total:.2f} €")
