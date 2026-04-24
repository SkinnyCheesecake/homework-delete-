import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def analisis_bivariable_estudiante(num_lista, n_muestras):
    np.random.seed(num_lista)
    horas_estudio = np.random.uniform(0, 20, n_muestras)
    pendiente = 2.0 + (num_lista % 5)
    ruido_factor = 20 / ( (num_lista % 3) + 1)
    error = np.random.normal( 0, ruido_factor, n_muestras )
    calificacion = (pendiente * horas_estudio) + error
    calificacion = np.clip(calificacion, 0, 100)
    df = pd.DataFrame({
        'Horas_Estudio': horas_estudio,
        'calificacion': calificacion
    })
    correlacion = df['Horas_Estudio'].corr(df['Calificacion'])
    print(f"--- Analisis para el alumno #{num_lista} ---")
    print(f"Tamano de la muestra: {n_muestras}")
    print(f"Coeficiente de correlacion de Pearson: {correlacion:.4f}")
    plt.figure(figsize = (8, 5))
    sns.regplot(x = 'Horas_Estudio', y = 'Calificacion', data = df,
                line_kws = {"color": "red"}, scatter_kws = {"alpha": 0.5})
    plt.title(f'Relacion horas vs caifiacion (Semilla: {num_lista})')
    plt.grid(True, linestyle = '---', alpha = 0.6)
    plt.show()
try:
    lista_input = int(input("Ingresa tu numero de lista: "))
    muestras_input = int(input("Ingresa el tamano de la muestra (ej. 50, 100): "))
    analisis_bivariable_estudiante(lista_input, muestras_input)
except ValueError:
    print("Error: por favor ingrese solo numero enteros")