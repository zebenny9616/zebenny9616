# Problème 5
# 3 floats, multiplier les deux premiers puis diviser le resultat par le 3eme. Max 3 chiffres après la virgule
import math

print("Veuillez entrez un premier nombre")
float1 = input()
print("Veuillez entrez un 2e nombre")
float2 = input()
print("Veuillez entrez un troisième nombre")
float3 = input()

Multiplication = float(float1*float2)

Division = float(Multiplication/float3)

print(Multiplication)
print(Division)

