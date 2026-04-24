import pandas as pd
import numpy as np

def limpieza_datos_dinamica(num_lista):
    np.random.seed(num_lista)
    n_registros = 50
    base_temp = 25.0
    ruido = np.random.normal(0, (num_lista % 10) + 1, n_registros)
    temperaturas = base_temp + ruido
    df = pd.DataFrame({"Temp_Sensor": temperaturas})
    indices_error = np.random.choice(df.index, size = 3, replace = False)
    df.loc[indices_error, 'Temp_Sensor'] *= (num_lista * 0.5)
    print(f"--- Reporte de limpieza (ID Alumno: {num_lista}) ---")
    print(f"Valor maximo detectado antes de la limpieza: {df['Temp_Sensor'].max():.2f}")
    umbral_z = 2.0 if num_lista % 2 == 0 else 3.0
    mu = df['Temp_Sensor'].mean()
    sigma = df['Temp_Sensor'].std()
    df['Z_Score'] = (df['Temp_Sensor'] - mu) / sigma
    df_limpio = df[df['Z_Score'].abs() <= umbral_z].copy()
    print(f"Umbral Z-Score aplicado: {umbral_z}")
    print(f"Registros eliminados por ser ruido/outliners: {len(df) - len(df_limpio)}")
    print(f"Nueva media post-limpieza: {df_limpio['Temp_Sensor'].mean():.2f}\n")
    return df_limpio.drop(columns = ['Z_Score']).head()
num_lista = 7
dataset_final = limpieza_datos_dinamica(num_lista)
print("Muestra del dataset limpio:")
print(dataset_final)