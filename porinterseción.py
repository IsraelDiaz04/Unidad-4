def solicitar_lista():
    s = input("Ingresa números (separados por espacios o comas): ").strip()
    s = s.replace(",", " ")
    try:
        return [int(x) for x in s.split()]
    except:
        print("Entrada inválida. Usa sólo números separados por espacios o comas.")
        return solicitar_lista()

def insercion_pasos(a):
    paso = 1
    print("Lista inicial:", a)
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        print(f"P{paso}: Tomar clave a[{i}]={clave}")
        paso += 1
        while j >= 0 and a[j] > clave:
            print(f"P{paso}: {a[j]} > {clave} -> desplazar a[{j}] a la posición {j+1}")
            a[j+1] = a[j]
            print(f"       Estado: {a}")
            j -= 1
            paso += 1
        a[j+1] = clave
        print(f"P{paso}: Insertar clave en posición {j+1} -> {a}")
        paso += 1
    print("Resultado final:", a)

if __name__ == "__main__":
    arr = solicitar_lista()
    if len(arr) > 60:
        r = input(f"La lista tiene {len(arr)} elementos. ¿Deseas ver todos los pasos? (s/n): ").strip().lower()
        if r != "s":
            print("Se canceló la impresión paso a paso por tamaño. Ejecuta de nuevo para proceder.")
        else:
            insercion_pasos(arr)
    else:
        insercion_pasos(arr)
