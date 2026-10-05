def validar_publi(publicacion):
    if publicacion["descripcion_publicacion"] == "":
        return False
    if publicacion["nombre_usuario"] =="":
        return False
    return True