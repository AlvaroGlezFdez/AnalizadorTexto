
# Proporciona una función de asistencia para ayudar al usuario a encontrar la ruta de un archivo .txt.
# Ofrece instrucciones visuales dependiendo del sistema operativo (Windows o Mac/Linux),
# para guiar al usuario en cómo copiar correctamente la ruta completa del archivo.





from limpiar_consola import consola_clear
import time


def conseguir_ruta():
    consola_clear()
    print("📁 No hay problema, vamos a ayudarte a conseguir la ruta del archivo.\n")
    print("🖥️  ¿Qué sistema operativo estás utilizando?")
    print("1️⃣  Windows")
    print("2️⃣  Mac o Linux")

    opcion_os = int(input("\nSeleccione una opción (1 ó 2): "))

    while opcion_os not in [1, 2]:
        print("❌ Respuesta no válida")
        opcion_os = int(input("Por favor, escoja entre 1 ó 2: "))

    if opcion_os == 1:
        consola_clear()
        print("🪟 Instrucciones para obtener la ruta del archivo en Windows:\n")

        instrucciones_w = [
            "📂 1. Abre la carpeta donde tienes el archivo",
            "🖱️ 2. Haz clic derecho sobre el archivo → 'Propiedades'",
            "📑 3. En la pestaña 'General', verás el campo 'Ubicación'",
            "📝 4. Copia esa ubicación y añádele '\\nombre_del_archivo.txt' al final",
            r"✅ 5. Ejemplo: C:\Users\Álvaro\Documents\proyecto\ejemplo_texto.txt"
        ]

        for instruccion in instrucciones_w:
            time.sleep(0.7)
            print(instruccion)

    elif opcion_os == 2:
        consola_clear()
        print("🐧 Instrucciones para obtener la ruta del archivo en Mac/Linux:\n")

        instrucciones_unix = [
            "📂 1. Abre la carpeta donde tienes el archivo",
            "🖱️ 2. Haz clic derecho sobre el archivo → 'Obtener información' (Mac) o 'Propiedades' (Linux)",
            "📑 3. Busca el campo 'Ruta' o 'Ubicación'",
            "📝 4. Copia esa ruta completa, incluyendo '/nombre_del_archivo.txt' al final",
            "✅ 5. Ejemplo: /home/alvaro/Documentos/proyecto/ejemplo_texto.txt"
        ]

        for instruccion in instrucciones_unix:
            time.sleep(0.7)
            print(instruccion)

    print("\n💡 Cuando tengas la ruta copiada, introdúcela cuando el programa te lo pida.")
    input("👉 Pulsa ENTER para continuar...")
    consola_clear()



