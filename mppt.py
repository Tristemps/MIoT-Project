import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Paramètres de la cellule photovoltaïque
I_SC = 1  # Courant de court-circuit (A)
K_I = 0.001  # Coefficient de température du courant (A/K)
T_C = 298  # Température de la cellule (K)
T_ref = 298  # Température de référence (K)
G = 1000  # Irradiation (W/m²)
G_ref = 1000  # Irradiation de référence (W/m²)
I_S = 1e-9  # Courant de saturation (A)
q = 1.602e-19  # Charge d'un électron (C)
N = 1  # Facteur d'idéalité
K = 1.381e-23  # Constante de Boltzmann (J/K)
R_S = 0.01  # Résistance série (Ω)
R_sh = 100  # Résistance shunt (Ω)

# Plage de tension pour laquelle on va calculer le courant
V = np.linspace(0, 1, 500)  # Tension variant de 0 à 1V avec 500 points

# Calcul du courant photogénéré
I_ph = (I_SC + K_I * (T_C - T_ref)) * (G / G_ref)

# Calcul du courant de diode (courant de diffusion)
I_d = I_S * (np.exp((q * (V + R_S * I_ph)) / (N * K * T_C)) - 1)

# Calcul du courant de shunt
I_sh = (V + R_S * I_ph) / R_sh

# Calcul du courant total en fonction de la tension
I = I_ph - I_d - I_sh

# Fonction pour calculer la tension en fonction du courant
def equation(V, I):
    return I_ph - I_S * (np.exp((q * (V + R_S * I)) / (N * K * T_C)) - 1) - (V + R_S * I) / R_sh - I

def calculate_voltage(I):
    V_solution = fsolve(equation, 0.5, args=(I))[0]
    return V_solution

# Exemple d'utilisation
I_input = 0.61  # Courant d'entrée (A)
V_output = calculate_voltage(I_input)

# Tracer la courbe I-V
plt.figure(figsize=(10, 6))
plt.plot(V, I, label='Courbe I-V', color='b')
plt.scatter(V_output, I_input, color='red', zorder=5)  # Ajouter le point spécifique
plt.annotate(f'({V_output:.2f}V, {I_input:.2f}A)', (V_output, I_input), textcoords="offset points", xytext=(10,-10), ha='center', color='red')
plt.title('Courbe caractéristique I-V')
plt.xlabel('Tension (V)')
plt.ylabel('Courant (A)')
plt.grid(True)
plt.legend()
plt.show()

print(f"Pour un courant de {I_input} A, la tension est {V_output:.4f} V")
