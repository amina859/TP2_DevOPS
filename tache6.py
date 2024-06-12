python
Copier le code
import numpy as np

# Définir une matrice 3x3
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

# Calculer l'inverse de la matrice
A_inv = np.linalg.inv(A)

print("Matrice A:")
print(A)
print("\nInverse de la matrice A:")
print(A_inv)