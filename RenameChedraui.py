import pandas as pd
import os

# Ruta del archivo Excel
excel_file = r"C:\\Users\\ocandanoza\\Downloads\\incidenciasMayo.xlsx"

# Carpeta donde están los archivos
carpeta_archivos = r"C:\\Users\\ocandanoza\\Downloads\\foliosMayo"

# Leer el Excel
df = pd.read_excel(excel_file, dtype=str)

# Mostrar nombres de columnas (para verificar)
print("Columnas detectadas con índice:")
for i, col in enumerate(df.columns):
    print(f"Índice {i}: {col}")

# Recorrer cada fila
for index, row in df.iterrows():

    # Columna B (nombre nuevo) - índice 1
    nombre_nuevo = str(row.iloc[1]).strip()

    # Columna K (nombre actual) - índice 10
    nombre_actual = str(row.iloc[10]).strip()

    ruta_actual = os.path.join(carpeta_archivos, nombre_actual)

    # Asegurar que el nombre nuevo tenga extensión .pdf
    if not nombre_nuevo.lower().endswith(".pdf"):
        nombre_nuevo += ".pdf"

    ruta_nueva = os.path.join(carpeta_archivos, nombre_nuevo)

    # Verificar si el archivo existe
    if os.path.exists(ruta_actual):
        os.rename(ruta_actual, ruta_nueva)
        print(f"Renombrado: {nombre_actual} → {nombre_nuevo}")
    else:
        print(f"No encontrado: {nombre_actual}")

print("Proceso terminado")