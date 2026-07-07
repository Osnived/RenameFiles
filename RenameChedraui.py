import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
env_path = Path(__file__).with_name('.env')
load_dotenv(dotenv_path=env_path)

# Ruta del archivo Excel
excel_file = os.getenv('EXCEL_FILE')

# Carpeta donde están los archivos
carpeta_archivos = os.getenv('CARPETA_ARCHIVOS')

# Leer el Excel
df = pd.read_excel(excel_file, dtype=str)

# Mostrar nombres de columnas (para verificar)
print("Columnas detectadas con índice:")
for i, col in enumerate(df.columns):
    print(f"Índice {i}: {col}")

# Recorrer cada fila
for index, row in df.iterrows():

    # En este archivo, los nombres reales de los archivos están en la columna "REEMPLAZAR"
    # y los nombres destino se toman de la columna "Name".
    nombre_actual_col = "REEMPLAZAR" if "REEMPLAZAR" in df.columns else df.columns[1]
    nombre_nuevo_col = "Name" if "Name" in df.columns else df.columns[0]

    nombre_actual = str(row[nombre_actual_col]).strip()
    nombre_nuevo = str(row[nombre_nuevo_col]).strip()

    ruta_actual = os.path.join(carpeta_archivos, nombre_actual)

    # Mantener la extensión original del archivo al renombrarlo
    extension_actual = os.path.splitext(nombre_actual)[1]
    if extension_actual and not os.path.splitext(nombre_nuevo)[1]:
        nombre_nuevo += extension_actual

    ruta_nueva = os.path.join(carpeta_archivos, nombre_nuevo)

    # Verificar si el archivo existe
    if os.path.exists(ruta_actual):
        os.rename(ruta_actual, ruta_nueva)
        print(f"Renombrado: {nombre_actual} → {nombre_nuevo}")
    else:
        print(f"No encontrado: {nombre_actual}")

print("Proceso terminado")
