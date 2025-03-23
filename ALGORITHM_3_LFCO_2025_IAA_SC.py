

def pda_acepta(cadena):
    """
    Reutilizamos el PDA del algoritmo 2.
    """
    pila = []

    for simbolo in cadena:
        if simbolo == 'a':
            pila.append('X')
        elif simbolo == 'b':
            if pila:
                pila.pop()
            else:
                return False
        else:
            return False

    return len(pila) == 0


def derivacion_izquierda(cadena):
  
    
    n = cadena.count('a')
    derivaciones = ["S"]
    actual = "S"

    for _ in range(n):
        actual = actual.replace("S", "aSb", 1)
        derivaciones.append(actual)

    actual = actual.replace("S", "ε", 1)
    derivaciones.append(actual)

    return derivaciones


def construir_arbol_desde_cadenas(nombre_archivo):
   
    try:
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()

        print("\nDerivaciones más a la izquierda (Algorithm 3):")

        for linea in lineas:
            if linea.startswith("Aceptada:") or linea.startswith("Rechazada:"):
                cadena = linea.strip().split(": ")[1]
                if pda_acepta(cadena):
                    print(f"\nCadena: {cadena}")
                    derivaciones = derivacion_izquierda(cadena)
                    for paso in derivaciones:
                        print(f"  → {paso}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    archivo_cadenas = "ALGORITHM_1_LFCO_2025_IAA_SC.txt"
    construir_arbol_desde_cadenas(archivo_cadenas)
