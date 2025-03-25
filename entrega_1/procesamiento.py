
# Contiene la lógica principal de análisis de texto, incluyendo:
# - División del texto en fragmentos para procesamiento multihilo.
# - Conteo de palabras y líneas.
# - Cálculo de estadísticas como palabra más frecuente, longitud media,
#   porcentaje de palabras únicas, y búsqueda por prefijo.
# Utiliza ThreadPoolExecutor para paralelizar el procesamiento por fragmentos.





from collections import Counter
from concurrent.futures import ThreadPoolExecutor


def dividir_texto(texto, num_partes):
    palabras = texto.split()
    total_palabras = len(palabras)
    tamaño_parte = total_palabras // num_partes
    resto = total_palabras % num_partes

    fragmentos = []
    inicio = 0

    for i in range(num_partes):
        fin = inicio + tamaño_parte
        if resto > 0:
            fin += 1
            resto -= 1

        fragmento = ' '.join(palabras[inicio:fin])
        fragmentos.append(fragmento)
        inicio = fin

    return fragmentos


def contar_palabras(fragmento):
    palabras = fragmento.split()
    contador = Counter(palabras)
    lineas = fragmento.count('\n') + 1

    resultado = {
        'contador': contador,
        'num_palabras': len(palabras),
        'num_lineas': lineas,
        'mas_frecuente': contador.most_common(1)[0] if contador else ("", 0)
    }

    return resultado


def procesar_texto_en_hilos(texto, num_hilos):
    fragmentos = dividir_texto(texto, num_hilos)

    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        resultados = list(executor.map(contar_palabras, fragmentos))

    total_contador = Counter()
    total_palabras = 0
    total_lineas = texto.count('\n') + (1 if texto.strip() else 0)

    for resultado in resultados:
        total_contador.update(resultado['contador'])
        total_palabras += resultado['num_palabras']
    resultado_final = {
        'contador_total': total_contador,
        'num_total_palabras': total_palabras,
        'num_total_lineas': total_lineas,
        'palabra_mas_frecuente': total_contador.most_common(1)[0] if total_contador else ("", 0)
    }

    return resultado_final





# === FUNCIONES EXTRA OPCIONALES ===

def contar_ocurrencias(contador, palabra):
    return contador[palabra]


def contar_lista_palabras(contador, palabras):
    resultado = {}
    for palabra in palabras:
        resultado[palabra] = contador[palabra]
    return resultado


def palabras_que_empiezan_por(contador, prefijo):
    coincidencias = {}
    for palabra, cantidad in contador.items():
        if palabra.lower().startswith(prefijo.lower()):
            coincidencias[palabra] = cantidad
    return coincidencias


def longitud_media_palabras(contador):
    total_letras = 0
    total_palabras = 0

    for palabra, cantidad in contador.items():
        total_letras += len(palabra) * cantidad
        total_palabras += cantidad

    if total_palabras == 0:
        return 0
    else:
        return total_letras / total_palabras


def porcentaje_palabras_unicas(contador):
    total = 0
    unicas = 0

    for palabra, cantidad in contador.items():
        total += cantidad
        if cantidad == 1:
            unicas += 1

    if total == 0:
        return 0
    else:
        return (unicas / total) * 100
