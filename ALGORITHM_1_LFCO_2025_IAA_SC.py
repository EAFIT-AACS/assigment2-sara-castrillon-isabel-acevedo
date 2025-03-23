import random


def generar_cadena_valida(n):
    """Genera una cadena válida de la forma a^n b^n."""
    return 'a' * n + 'b' * n

def generar_cadena_invalida():
    """Genera una cadena inválida con el alfabeto {a, b}."""
    opciones_invalidas = [
        'aab', 'abb', 'ba', 'abab', 'aaabb', 'abbb'
    ]
    return random.choice(opciones_invalidas)

def mutar_cadena(cadena, es_valida=True):
    """
    Realiza una mutación sobre una cadena:
    - Al ser válida: la hace más larga pero sigue siendo cumpliendo la condición.
    - Al ser inválida: altera el orden o repite letras para seguir siendo inválida.
    """
    if es_valida:
        n = cadena.count('a') + 1  # incrementar n
        return generar_cadena_valida(n)
    else:
        mutaciones = [
            lambda s: s[::-1],                           # invierte
            lambda s: s.replace('a', 'aa', 1),           # duplicar una 'a'
            lambda s: s.replace('b', 'bb', 1),           # duplicar una 'b'
            lambda s: s.replace('ab', 'ba', 1),          # cambiar orden
        ]
        mutacion = random.choice(mutaciones)
        return mutacion(cadena)



def main():
    cadenas_aceptadas = []
    cadenas_rechazadas = []

    # Generar cadenas válidas y mutadas
    for i in range(2, 4):
        base = generar_cadena_valida(i)
        mutada = mutar_cadena(base, es_valida=True)
        cadenas_aceptadas.extend([base, mutada])

    # Generar cadenas inválidas y mutadas
    for _ in range(2):
        base = generar_cadena_invalida()
        mutada = mutar_cadena(base, es_valida=False)
        cadenas_rechazadas.extend([base, mutada])

    # Mostrar por consola
    print("Cadenas válidas:")
    for c in cadenas_aceptadas:
        print(f"Aceptada: {c}")

    print("\nCadenas inválidas:")
    for c in cadenas_rechazadas:
        print(f"Rechazada: {c}")

    # Guardar en el archivo
    with open("ALGORITHM_1_LFCO_2025_IAA_SC.txt", "w") as f:
        f.write("Cadenas válidas:\n")
        for c in cadenas_aceptadas:
            f.write(f"Aceptada: {c}\n")
        f.write("\nCadenas inválidas:\n")
        for c in cadenas_rechazadas:
            f.write(f"Rechazada: {c}\n")

if __name__ == "__main__":
    main()
