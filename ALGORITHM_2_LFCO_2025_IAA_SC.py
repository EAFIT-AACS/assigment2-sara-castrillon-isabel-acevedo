

def pda_acepta(cadena):
   
    pila = []

    for simbolo in cadena:
        if simbolo == 'a':
            pila.append('X')  # Apilar símbolo por cada 'a'
        elif simbolo == 'b':
            if pila:
                pila.pop()  # Desapilar por cada 'b'
            else:
                return False  # Más 'b' que 'a', error
        else:
            return False  # Símbolo no permitido (solo 'a' y 'b')

    return len(pila) == 0  # Si la pila está vacía al final, la cadena es válida


def evaluar_cadenas_desde_archivo(nombre_archivo):
    """
    Lee el archivo que genera el algoritmo 1, evalúa cada cadena con el PDA,
    e imprime si la acepta o no.
    """
    try:
        with open(nombre_archivo, "r") as f:
            lineas = f.readlines()

        print("Resultados PDA (Algorithm 2):\n")
        for linea in lineas:
            if linea.startswith("Aceptada:") or linea.startswith("Rechazada:"):
                cadena = linea.strip().split(": ")[1]
                resultado = pda_acepta(cadena)
                estado = "Aceptada por el PDA" if resultado else "Rechazada por el PDA"
                print(f"{cadena} → {estado}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


if __name__ == "__main__":
    archivo_cadenas = "ALGORITHM_1_LFCO_2025_IAA_SC.txt"
    evaluar_cadenas_desde_archivo(archivo_cadenas)
