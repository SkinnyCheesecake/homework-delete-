import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def preprocesamiento_perzonaliado(num_lista):
    np.random.seed(num_lista)
    print(f"--- Iniciando preprocesamiento para el alumno con el numero de lista: {num_lista} ---")
    n_muestras = 100
    datos = {
        'Edad': np.random.randint(10, 70, n_muestras),
        'Ingresos_Anueles': np.random.normal(5000, 15000, n_muestras),
        'Monto_Prestamo': np.random.uniform(5000, 30000, n_muestras)
    }
    df = pd.DataFrame(datos)
    proporcion_nulos = 0.1 if num_lista % 2 == 0 else 0.15
    for col in df.columns:
            df.loc[df.sample(frac=proporcion_nulos).index, col] = np.nan
    print(f"Valores nulos generados (basado en proporcion {proporcion_nulos}):\n{df.isnull().sum()}\n")
    df_limpio = df.fillna(df.mean())
    scaler = StandardScaler()
    df_escalado = pd.DataFrame(scaler.fit_transform(df_limpio), columns=df.columns)
    return df_escalado.head()
mi_numero = 7 #numero de lista
resultado = preprocesamiento_perzonaliado(mi_numero)
print("Vista previa de los datos preprocesados y normalizados")
print(resultado)