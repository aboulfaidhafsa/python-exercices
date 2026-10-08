def verifier_temperature(temperature):
    if temperature < 0:
        etat = "gel"
    elif temperature < 15:
        etat = "froid"
    elif temperature < 25:
        etat = "doux"
    else:
        etat = "chaud"
        
    print(f"{temperature} degre c ; {etat}")

# Test des valeurs demandées pour vérifier les cas limites
temperatures = [-3, 0, 15, 31]

for t in temperatures:
    verifier_temperature(t)

def verifier_annee_bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        print(f"{annee} ; bissextille")
    else:
        print(f"{annee} ; non bissextille")


