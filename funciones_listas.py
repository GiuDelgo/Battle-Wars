
def validar_lista (lista: list)->None:
    """Valida que el parametro sea de tipo lista

    Args:
        lista (list): parametro a verifiar como lista

    Raises:
        TypeError: en caso de que no se haya pasado una lista la función devuleve un error de tipo
    """
    if not isinstance(lista,list):
        raise TypeError("Se esperaba una lista")

def convert_csv (diccionario: dict)->dict:
    """Convierte un archivo formato csv en diccionario

    Args:
        diccionario (dict): diccionario vacío

    Returns:
        list: diccionario contenedor de los datos del archivo csv
    """

    with open("./src/preferencias.csv", "r", encoding="utf-8") as archivo:      
        encabezado = archivo.readline().strip("\n").split(",")
        linea = archivo.readline().strip("\n").split(",")
        for i in range (len(encabezado)): 
            try:
                if encabezado[i] == "volumen":
                    diccionario[encabezado[i]] = float(linea[i])
                else:
                    diccionario[encabezado[i]] = int(linea[i])
            except IndexError:
                print(f"Índice {i} fuera de rango. Verifique la longitud de las líneas en el CSV.")
            except ValueError:
                print(f"Error al convertir el valor {linea[i]} en la columna {encabezado[i]}")
    return diccionario

def swap_lista (lista: list, i: int, j: int)-> None:
        """intercambia dos valores consecutivos de una lista

        Args:
            lista (list): lista cuyos valores se intercambian
            i (int): indice i
            j (int): indice j
        """
        aux = lista[i]
        lista[i] = lista [j]
        lista[j] = aux

def ordenar_lista (comparator, lista: list)->None: 
        """ordena la lista según un criterio

        Args:
            comparator (_type_): función que establece el criterio de ordenamiento
            lista (list): lista a ordenar
        """
        validar_lista (lista)
        for i in range (len(lista)-1):
            for j in range (i+1, len(lista)):
                if comparator(lista[i], lista[j]):
                    swap_lista (lista, i, j)