from src.scanner import obtener_info
from src.db_manager import guardar_datos

datos = obtener_info()
guardar_datos(datos)
print("Auditoría finalizada.")