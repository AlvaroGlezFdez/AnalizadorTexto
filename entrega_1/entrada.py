
# Este script gestiona la entrada del texto que será analizado.
# Permite al usuario introducir el texto manualmente o cargarlo desde un archivo .txt. 
# Incluye validación de opciones, ayuda para obtener la ruta del archivo
# y devuelve el texto para su procesamiento.






import time
from limpiar_consola import consola_clear
from extras import conseguir_ruta


def obtener_texto():
    consola_clear()
    print("📥 Bienvenido al analizador de texto")
    print("\nSeleccione cómo desea introducir el texto:")
    print("1️⃣  Introducir texto manualmente")
    print("2️⃣  Cargar texto desde archivo .txt")

    opcion = int(input("\nEscoja una opción (1 o 2): "))

    while opcion not in [1, 2]:
        print("❌ Opción no válida.")
        opcion = int(input("Por favor, elija 1 o 2: "))

    consola_clear()

    if opcion == 1:
        print("📝 Introducción de texto manual")
        time.sleep(1)
        consola_clear()
        print("Introduce tu texto línea por línea.")
        print("Pulsa ENTER dos veces para finalizar.\n")

        lineas = []
        while True:
            linea = input()
            if linea == "":
                break
            lineas.append(linea)

        texto = "\n".join(lineas)
        consola_clear()
        return texto

    elif opcion == 2:
        print("📂 Lectura desde archivo")
        print("¿Sabes cómo obtener la ruta del archivo?")
        print("1️⃣  Sí, quiero introducirla directamente")
        print("2️⃣  No, necesito ayuda")
        opcion_ruta = int(input("Seleccione 1 o 2: "))

        while opcion_ruta not in [1, 2]:
            print("❌ Opción no válida.")
            opcion_ruta = int(input("Por favor, elija 1 o 2: "))

        if opcion_ruta == 2:
            conseguir_ruta()

        consola_clear()
        ruta = input("📎 Introduce la ruta del archivo (.txt): ").strip()

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                texto = archivo.read()
                consola_clear()
                return texto
        except FileNotFoundError:
            print("❌ Archivo no encontrado.")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

        return None
