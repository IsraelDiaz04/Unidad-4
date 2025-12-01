def solicitar_lista():
    s = input("Ingresa números (separados por espacios o comas): ").strip()
    s = s.replace(",", " ")
    try:
        return [int(x) for x in s.split()]
    except:
        print("Entrada inválida. Usa sólo números separados por espacios o comas.")
        return solicitar_lista()

def seleccion_pasos(a):
    n = len(a)
    paso = 1
    print("Lista inicial:", a)
    for i in range(n):
        min_idx = i
        print(f"P{paso}: Iteración i={i}, supuesto mínimo a[{min_idx}]={a[min_idx]}")
        paso += 1
        for j in range(i+1, n):
            print(f"P{paso}: Comparar a[{j}]={a[j]} con actual mínimo a[{min_idx}]={a[min_idx]}")
            if a[j] < a[min_idx]:
                min_idx = j
                print(f"P{paso}: -> Nuevo mínimo a[{min_idx}]={a[min_idx]}")
            else:
                print(f"P{paso}: -> No cambia el mínimo")
            paso += 1
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            print(f"P{paso}: Intercambio a[{i}] <-> a[{min_idx}] -> {a}")
        else:
            print(f"P{paso}: Ningún intercambio necesario -> {a}")
        paso += 1
    print("Resultado final:", a)

if __name__ == "__main__":
    arr = solicitar_lista()
    if len(arr) > 60:
        r = input(f"La lista tiene {len(arr)} elementos. ¿Deseas ver todos los pasos? (s/n): ").strip().lower()
        if r != "s":
            print("Se canceló la impresión paso a paso por tamaño. Ejecuta de nuevo para proceder.")
        else:
            seleccion_pasos(arr)
    else:
        seleccion_pasos(arr)
