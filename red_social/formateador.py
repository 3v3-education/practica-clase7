def crear_separador():
    return "-" * 120

def formatear_publi(publicacion):
    descripcion = publicacion["descripcion_publicacion"]
    estado = publicacion["estado"]
    usuario = publicacion["nombre_usuario"]
    likes = publicacion["cantidad_likes"]
    return f"""Descripcion: {descripcion} | Usuario: {usuario} | Estado_ {estado} | Likes: {likes}"""

def listar_publis (lista_publis):
    for publi in lista_publis:
        print(crear_separador())
        print(formatear_publi(publi))
