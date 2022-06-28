lista=["hola", 2, "mundoo", 4]

lista_dos=["hola jas", 5, "asdfadoo", 4]


def devolver_num_invertidos(parametro_lista):
    nueva_lista = []
    #recorrer la lista
    for elemento in parametro_lista:
        # chequeo si es un numero
        if type(elemento) == int:
            # agregar el elemento a la lista
            nueva_lista.append(elemento)
    return nueva_lista


resultado_uno = devolver_num_invertidos(lista)
print(resultado_uno)

resultado_dos = devolver_num_invertidos(lista_dos)
print(resultado_dos)