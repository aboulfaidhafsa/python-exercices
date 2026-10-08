from outils import convertir_note, mention, moyenne

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes_valides = []
notes_ignorees = 0

for n in notes_brutes:
    valeur = convertir_note(n)
    if valeur is not None:
        notes_valides.append(valeur)
    else:
        notes_ignorees += 1

moy = moyenne(notes_valides)
men = mention(moy)

print(f"Notes ignorées : {notes_ignorees}")
print(f"Moyenne : {moy:.2f}")
print(f"Mention : {men}")