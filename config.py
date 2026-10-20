import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Configuración del sistema
UNIX_TRIGGER_URL = os.getenv('UNIX_TRIGGER_URL')
RUTA_RED = os.getenv('RUTA_RED')
ARCHIVO_ORIGEN = os.getenv('ARCHIVO_ORIGEN')
ARCHIVO_SALIDA = os.getenv('ARCHIVO_SALIDA')
COLUMNA_MONTO = os.getenv('COLUMNA_MONTO')

def verificar_configuracion():
    """Verifica que todas las variables críticas estén presentes"""
    requeridas = [UNIX_TRIGGER_URL, RUTA_RED, ARCHIVO_ORIGEN, ARCHIVO_SALIDA, COLUMNA_MONTO]
    if not all(requeridas):
        raise ValueError("⚠️ Faltan variables en el archivo .env. Revisa la configuración.")
    print("✅ Configuración cargada correctamente.")