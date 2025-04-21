def crear_nodo(valor):
    return [valor, None, None]

def insertar_nodo(raiz, valor):
    nuevo_nodo = crear_nodo(valor)
    posicion = raiz
    while True:
        lado = input(f"¿Insertar {valor} a la izquierda o derecha de {posicion[0]}? (i/d): ").lower()
        if lado == 'i':
            if posicion[1] is None:
                posicion[1] = nuevo_nodo
                break
            else:
                posicion = posicion[1]
        elif lado == 'd':
            if posicion[2] is None:
                posicion[2] = nuevo_nodo
                break
            else:
                posicion = posicion[2]
        else:
            print("Entrada inválida. Usa 'i' o 'd'.")

def peso_arbol(nodo):
    if nodo is None:
        return 0
    return 1 + peso_arbol(nodo[1]) + peso_arbol(nodo[2])

def altura_arbol(nodo):
    if nodo is None:
        return 0
    izquierda = altura_arbol(nodo[1])
    derecha = altura_arbol(nodo[2])
    return 1 + max(izquierda, derecha)

def orden_arbol():  
    return 2

n = int(input("¿Cuántos nodos deseas ingresar?: "))
if n <= 0:
    print("Debes ingresar al menos un nodo.")
else:
    valor_raiz = input("Ingrese el valor del nodo raíz: ")
    arbol = crear_nodo(valor_raiz)
    for _ in range(n - 1):
        valor = input("Ingrese el valor del nuevo nodo: ")
        insertar_nodo(arbol, valor)

    print("\n--- Resultados ---")
    print(f"Peso del árbol (cantidad de nodos): {peso_arbol(arbol)}")
    print(f"Orden del árbol (máx hijos por nodo): {orden_arbol()}")
    print(f"Altura del árbol: {altura_arbol(arbol)}")