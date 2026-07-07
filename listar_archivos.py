import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env desde la misma carpeta
load_dotenv(Path(__file__).with_name('.env'))

carpeta = os.getenv('CARPETA_ARCHIVOS')

if not carpeta:
    raise SystemExit('No se encontró CARPETA_ARCHIVOS en el .env')

carpeta_path = Path(carpeta)

if not carpeta_path.exists() or not carpeta_path.is_dir():
    raise SystemExit(f'La carpeta no existe o no es válida: {carpeta_path}')

archivos = sorted(carpeta_path.iterdir(), key=lambda p: p.name.lower())

print(f'Archivos encontrados en: {carpeta_path}')
print('---')
for archivo in archivos:
    if archivo.is_file():
        print(archivo.name)
