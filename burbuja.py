def solicitar_lista():
    s = input("Ingresa números (separados por espacios o comas): ").strip()
    s = s.replace(",", " ")
    try:
        return [int(x) for x in s.split()]
    except:
        print("Entrada inválida. Usa sólo números separados por espacios o comas.")
        return solicitar_lista()

def burbuja_pasos(a):
    n = len(a)
    paso = 1
    print("Lista inicial:", a)
    for i in range(n):
        for j in range(0, n - i - 1):
            print(f"P{paso}: Comparar a[{j}]={a[j]} con a[{j+1}]={a[j+1]}")
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(f"P{paso}: -> Intercambio -> {a}")
            else:
                print(f"P{paso}: -> No intercambia -> {a}")
            paso += 1
    print("Resultado final:", a)

if __name__ == "__main__":
    arr = solicitar_lista()
    if len(arr) > 60:
        r = input(f"La lista tiene {len(arr)} elementos. ¿Deseas ver todos los pasos? (s/n): ").strip().lower()
        if r != "s":
            print("Se canceló la impresión paso a paso por tamaño. Ejecuta de nuevo para proceder.")
        else:
            burbuja_pasos(arr)
    else:
        burbuja_pasos(arr)
