
# Programa princiapl donde importamos todos los modulos
# contiene un menú infinito (While True) que solo se romperá cuando el usuario quiera salir



from entrada import obtener_texto
from procesamiento import (
    procesar_texto_en_hilos,
    contar_ocurrencias,
    contar_lista_palabras
)

def mostrar_menu_opciones_extra(contador_total):
    while True:
        print("\n🔧 MENÚ DE FUNCIONES EXTRA:")
        print("1️⃣  Buscar una palabra")
        print("2️⃣  Buscar varias palabras")
        print("3️⃣  Ver Top N palabras más frecuentes")
        print("4️⃣  Buscar palabras que empiecen por una letra o prefijo")
        print("5️⃣  Calcular longitud media de palabras")
        print("6️⃣  Calcular porcentaje de palabras únicas")
        print("0️⃣  Salir del menú")

        opcion = input("\nElige una opción (0-6): ").strip()

        if opcion == "0":
            print("👋 Saliendo del menú de funciones extra.")
            break

        elif opcion == "1":
            palabra = input("🔎 Escribe la palabra: ").strip()
            print(f"✅ La palabra '{palabra}' aparece {contador_total[palabra]} veces.")

        elif opcion == "2":
            entrada = input("✍️ Escribe varias palabras separadas por espacio: ").strip()
            lista = entrada.split()
            resultado = contar_lista_palabras(contador_total, lista)
            print("\n📌 Resultados:")
            for p, c in resultado.items():
                print(f"🔎 '{p}': {c} veces")

        elif opcion == "3":
            top = int(input("🏅 ¿Cuántas palabras quieres ver?: "))
            print(f"\n🏆 Top {top} palabras más frecuentes:")
            for palabra, count in contador_total.most_common(top):
                print(f"🔹 {palabra}: {count} veces")

        elif opcion == "4":
            prefijo = input("🔡 Escribe la letra o prefijo: ").strip().lower()
            coincidencias = {p: c for p, c in contador_total.items() if p.lower().startswith(prefijo)}
            print(f"\n🔍 Palabras que empiezan por '{prefijo}':")
            for p, c in coincidencias.items():
                print(f"🔸 {p}: {c} veces")

        elif opcion == "5":
            total_letras = sum(len(p) * c for p, c in contador_total.items())
            total_palabras = sum(contador_total.values())
            media = total_letras / total_palabras if total_palabras > 0 else 0
            print(f"\n📏 Longitud media de palabras: {media:.2f} letras")

        elif opcion == "6":
            total = sum(contador_total.values())
            únicas = len([p for p, c in contador_total.items() if c == 1])
            porcentaje = (únicas / total) * 100 if total > 0 else 0
            print(f"\n🧠 Porcentaje de palabras únicas: {porcentaje:.2f}%")

        else:
            print("❌ Opción no válida. Intenta de nuevo.")


def main():
    texto = obtener_texto()

    if texto:
        resultado = procesar_texto_en_hilos(texto, num_hilos=4)

        print("\n📊 Estadísticas del texto:\n")
        print(f"🔢 Total de palabras: {resultado['num_total_palabras']}")
        print(f"📈 Total de líneas: {resultado['num_total_lineas']}")
        print(f"🏆 Palabra más frecuente: '{resultado['palabra_mas_frecuente'][0]}' ({resultado['palabra_mas_frecuente'][1]} veces)")

        mostrar_menu_opciones_extra(resultado['contador_total'])

    else:
        print("⚠️ No se pudo cargar el texto. Finalizando programa.")


if __name__ == "__main__":
    main()
