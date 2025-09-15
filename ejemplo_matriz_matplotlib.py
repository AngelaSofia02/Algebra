import matplotlib.pyplot as plt
import numpy as np

matriz = np.arange(1, 26).reshape(5, 5)

print("Matriz:")
print(matriz)

plt.imshow(matriz, cmap='viridis', interpolation='nearest')
plt.colorbar(label="Valor de la celda")
plt.title("Visualización de una matriz con Matplotlib")
plt.xlabel("Columnas")
plt.ylabel("Filas")
plt.show()

for i in range(matriz.shape[0]):
    plt.plot(matriz[i], label=f"Fila {i+1}")

plt.title("Filas de la matriz representadas como curvas")
plt.xlabel("Índice de columna")
plt.ylabel("Valor")
plt.legend()
plt.show()
