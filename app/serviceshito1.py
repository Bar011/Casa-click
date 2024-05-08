from app.models import Inmueble ,Usuario ,Region, Comuna
from django.core.exceptions import ObjectDoesNotExist

def obtener_inmuebles():
    inmueble = Inmueble.objects.all()
    
# Imprimir los inmuebles de manera ordenada
    for inmueble in inmueble:
        print(f"Inmueble: {inmueble.nombre}")
        print(f"Dirección: {inmueble.direccion}")
        print(f"Ciudad: {inmueble.comuna}")
        print(f"Tipo: {inmueble.tipo_de_inmueble}")
        print(f"Propietario: {inmueble.propietario}")
        print()


def crear_inmueble(nombre,direccion,descripcion,imagen,precio ,disponible,m2_construidos, comuna_id, m2_terreno,cantidad_estacionamientos, cantidad_habitaciones,
cantidad_banos,tipo_de_inmueble,usuario_id):
    
    #Le paso el id como parametro y lo transforma al objeto
    comuna = Comuna.objects.get(pk=comuna_id)
    #comuna = Comuna.objects.get(nombre = "Providencia")
    usuario = Usuario.objects.get(pk=usuario_id)
    
    inmueble = Inmueble.objects.create(
        nombre=nombre,
        direccion=direccion,
        descripcion=descripcion,
        imagen=imagen,
        precio=precio,
        comuna=comuna, # Se obtiene en la BD
        disponible=disponible,
        m2_construidos=m2_construidos,
        m2_terreno=m2_terreno,
        cantidad_estacionamientos=cantidad_estacionamientos,
        cantidad_habitaciones=cantidad_habitaciones,
        cantidad_banos=cantidad_banos,
        tipo_de_inmueble=tipo_de_inmueble,
        propietario=usuario, # Se obtiene en la BD
    )

    return inmueble
  
 
def actualizar_descrp_inmueble(id_inmueble,new_descrip):
    Inmueble.objects.filter(pk=id_inmueble).update(descripcion=new_descrip)
    print("¡Descripción actualizada exitosamente!")
 
 
def eliminar_inmueble(id_inmueble):
    Inmueble.objects.get(id=id_inmueble).delete()
    print("¡Inmueble eliminado con exito!")