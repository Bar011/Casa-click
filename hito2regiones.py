import os
import django
from django.db import connection

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlydepas.settings')
django.setup()

# Consulta SQL para obtener los inmuebles por comunas
consulta_sql = """
    #Por elaborar
"""

# Ejecutar la consulta SQL
with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

# Guardar los resultados en un archivo de texto
with open('inmuebles_por_region.txt', 'w') as archivo:
    for nombre, descripcion in resultados:
        archivo.write(f"Nombre: {nombre}\nDescripción: {descripcion}\n\n")