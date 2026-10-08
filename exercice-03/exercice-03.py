temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

moyenne = sum(temperatures) / len(temperatures)
print(f"Moyenne ; {round(moyenne, 2)}")
print(f"Min ; {min(temperatures)} / Max ; {max(temperatures)}")


jours_sup_15 = 0
for t in temperatures:
    if t > 15:
        jours_sup_15 += 1
print(f"jours >15 °C ; {jours_sup_15}")


fahrenheit = [t * 9 / 5 + 32 for t in temperatures]
print(f"Fahrenheit ; {fahrenheit}")

for i, t in enumerate(temperatures, start=1):  
    print(f"jour {i} ; {t} °C")