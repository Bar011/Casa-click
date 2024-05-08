import os
import django
from django.db import connection

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlydepas.settings')
django.setup()

# Consulta SQL para obtener los inmuebles por comunas
consulta_sql = """
    SELECT r.nombre AS region, i.nombre AS inmueble_nombre, i.descripcion AS inmueble_descripcion
    FROM app_inmueble AS i
    INNER JOIN app_comuna AS c ON i.comuna_id = c.id
    INNER JOIN app_region AS r ON c.region_id = r.id
    WHERE i.disponible = TRUE
    ORDER BY r.nombre
"""

# Ejecutar la consulta SQL
with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

# Guardar los resultados en un archivo de texto
resultados_file = 'inmuebles_por_regiones.txt'
with open(resultados_file, "w") as file:
    region_actual = None
    for region, inmueble_nombre, inmueble_descripcion in resultados:
        if region != region_actual:
            if region_actual:
                file.write("\n")
            file.write(f"Region: {region}\n")
            region_actual = region
        file.write(f"Inmueble: {inmueble_nombre}\n")
        file.write(f"Descripcion: {inmueble_descripcion}\n")
print("¡Archivo creado exitosamente!")