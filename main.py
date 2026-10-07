#importacion de un modulo
import red_social.datos as datos
import red_social.formateador as formateador
from red_social.datos import publicaciones


#importacion con alias
import red_social.formateador as fmt

#Ejemplo del acceso a un dato del modulo con notacion punto

print(publicaciones[0])

#Importacion de una funcion especifica
#Con notacion punto

fmt.listar_publis(datos.publicaciones)

#Con from..import
from red_social.formateador import listar_publis 
listar_publis(publicaciones)

from red_social.validaciones import validar_publi
for publi in publicaciones:    
    if validar_publi(publi):        
        print(f"La descripcion '{publi["descripcion_publicacion"]}' es válida.")    
    else:        
        print(f"El post con ID {publi['id']} tiene datos incompletos.")


#Importacion de varios elementos
from red_social.formateador import crear_separador, formatear_publi
print(crear_separador())
print(formatear_publi(publicaciones[0]))

#_____________ARCHIVOS____________
ARCHIVO_PUBLIS = "publicaciones.txt"

publicacion = {
    "id": 67654,
    "nombre_usuario": "Juan.Perez",
    "ubicacion_usuario": "Madrid, España",
    "descripcion_publicacion": "Aprendiendo Python.",
    "cantidad_likes": 150,
    "estado": True,
    "comentarios": ["¡Muy interesante!"],
    "puntuacion": 4.5
}

def guardar_publi(publicacion):
    with open("publicaciones.txt","a", encoding="utf-8") as archivo:
        linea = f"{publicacion["id"]}|{publicacion["nombre_usuario"]}|{publicacion["ubicacion_usuario"]}|{publicacion["descripcion_publicacion"]}|{publicacion["cantidad_likes"]}|{publicacion["estado"]}|{publicacion["comentarios"]}|{publicacion["puntuacion"]}\n"        
        archivo.write (linea)

guardar_publi(publicacion)


def listar_publis():
    try:
        with open(ARCHIVO_PUBLIS, "r", encoding="utf-8") as archivo:
            print("Publicaciones guardadas: ")
            for linea in archivo:
                contenido = linea.strip()
                print(f"---{contenido}")
    except FileNotFoundError:
        print("Todavia no hay publicaciones guardadas")

listar_publis()

def buscar_publi(termino):
    resultados = []
    try:
        with open(ARCHIVO_PUBLIS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                descripcion = linea.strip()
                if termino.lower() in descripcion.lower():
                    resultados.append(descripcion)
    except FileNotFoundError:
        print("Todavia no hay publicaciones guardadas")
    return resultados

print("\n Resultados de busqueda")
resultados = buscar_publi("python")
for publi in resultados:
    print(f"--{publi}")

#Manejo de rutas
from pathlib import Path
ruta_archivo = Path("data") / "publicaciones.txt"
print(ruta_archivo)

carpeta_data = Path("data")
carpeta_data.mkdir(exist_ok=True)

#Guardar una publi usando pathlib
CARPETA_DATA = Path("data")
ARCHIVO_PUBLICACIONES = CARPETA_DATA / "publicaciones.txt"

def preparar_archivos():
    CARPETA_DATA.mkdir(exist_ok=True)

def guardar_publi(publicacion):
    preparar_archivos()
    with open(ARCHIVO_PUBLICACIONES, "a",encoding="utf-8") as archivo:
        linea = f"{publicacion["id"]}|{publicacion["nombre_usuario"]}|{publicacion["ubicacion_usuario"]}|{publicacion["descripcion_publicacion"]}|{publicacion["cantidad_likes"]}|{publicacion["estado"]}|{publicacion["comentarios"]}|{publicacion["puntuacion"]}\n"        
        archivo.write (linea)

def listar_publis():
    if not  ARCHIVO_PUBLICACIONES.exists():
        print("Todavia no hay publicaciones guardadas")
        return
    with open(ARCHIVO_PUBLICACIONES,"r", encoding="utf-8") as archivo:
        print("Publicaciones guardadas: ")
        for linea in archivo:
            contenido = linea.strip()
            print(f"---{contenido}")

guardar_publi(publicacion)

#Path(__file) para ubicar el proyecto

BASE_DIR = Path(__file__).parent

CARPETA_DATA = BASE_DIR / "data"
ARCHIVO_PUBLIS = CARPETA_DATA / "publicaciones.txt"
print(BASE_DIR)
print(ARCHIVO_PUBLIS)


"""CODIGO NUEVA FUNCIONALIDAD"""