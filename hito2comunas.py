import os
import django
from django.db import connection

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlydepas.settings')
django.setup()

# Consulta SQL para obtener los inmuebles por comunas
consulta_sql = """
    SELECT c.nombre AS comuna, i.nombre AS nombre_inmueble, i.descripcion
    FROM app_inmueble i
    JOIN app_comuna c ON i.comuna_id = c.id
    WHERE i.disponible = TRUE
"""

# Ejecutar la consulta SQL
with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

# Guardar los resultados en un archivo de texto
resultados_file = 'inmuebles_por_comuna.txt'
with open(resultados_file, "w") as file:
    for row in resultados:
        comuna, nombre_inmueble, descripcion = row
        file.write(f"Comuna: {comuna}\n")
        file.write(f"Nombre del inmueble: {nombre_inmueble}\n")
        file.write(f"Descripcion: {descripcion}\n")
        file.write("\n")
print("¡Archivo creado exitosamente!")