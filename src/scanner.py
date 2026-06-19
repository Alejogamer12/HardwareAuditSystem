import psutil
import platform

def obtener_info():
    # Obtener nombre del procesador
    cpu = platform.processor()
    
    # Obtener memoria RAM total (en GB)
    mem = psutil.virtual_memory().total
    ram_gb = round(mem / (1024**3), 2)
    
    # Obtener espacio en disco total (en GB)
    disk = psutil.disk_usage('/').total
    disk_gb = round(disk / (1024**3), 2)

    return {
        "cpu": cpu,
        "ram": f"{ram_gb} GB",
        "disco": f"{disk_gb} GB"
    }