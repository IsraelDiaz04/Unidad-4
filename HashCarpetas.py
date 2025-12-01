import os
import shutil
import hashlib

def calcular_bucket(nombre_archivo, num_buckets):
    h = hashlib.sha256(nombre_archivo.encode('utf-8')).hexdigest()
    valor_entero = int(h, 16)
    return valor_entero % num_buckets, h

def asegurar_ruta_unica(destino):
    if not os.path.exists(destino):
        return destino
    base, ext = os.path.splitext(destino)
    contador = 1
    nuevo = f"{base}_{contador}{ext}"
    while os.path.exists(nuevo):
        contador += 1
        nuevo = f"{base}_{contador}{ext}"
    return nuevo

def organizar_por_hash(ruta_carpeta, num_buckets):
    if not os.path.isdir(ruta_carpeta):
        print("La ruta indicada no es una carpeta válida.")
        return
    elementos = os.listdir(ruta_carpeta)
    archivos = [f for f in elementos if os.path.isfile(os.path.join(ruta_carpeta, f))]

    if not archivos:
        print("No hay archivos en la carpeta indicada.")
        return

    print(f"\nProcesando {len(archivos)} archivos en: {ruta_carpeta}")
    for i in range(num_buckets):
        carpeta_bucket = os.path.join(ruta_carpeta, f"bucket_{i}")
        if not os.path.exists(carpeta_bucket):
            os.makedirs(carpeta_bucket)

    for nombre in archivos:
        ruta_origen = os.path.join(ruta_carpeta, nombre)
        bucket_index, hash_hex = calcular_bucket(nombre, num_buckets)
        carpeta_dest = os.path.join(ruta_carpeta, f"bucket_{bucket_index}")

        print("\n---------------------------")
        print(f"Archivo: {nombre}")
        print(f"Hash SHA-256 (hex): {hash_hex}")
        print(f"Valor entero (mod {num_buckets}) -> bucket {bucket_index}")
        destino_propuesto = os.path.join(carpeta_dest, nombre)
        destino_final = asegurar_ruta_unica(destino_propuesto)

        shutil.move(ruta_origen, destino_final)
        if destino_final == destino_propuesto:
            print(f"Movido a: {destino_final}")
        else:
            print(f"Nombre en destino ya existía. Movido y renombrado a: {destino_final}")

    print("\nOrganización por hash completada.")

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la carpeta a organizar: ").strip()
    try:
        buckets = int(input("Ingresa el número de buckets (por ejemplo 10): ").strip())
        if buckets <= 0:
            raise ValueError
    except ValueError:
        print("Número de buckets inválido. Usando 10 por defecto.")
        buckets = 10
    organizar_por_hash(ruta, buckets)
