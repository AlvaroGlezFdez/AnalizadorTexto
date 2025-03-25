
# Analizador de Texto Multihilo

Este proyecto es una aplicación que permite analizar textos desde la terminal o mediante una interfaz gráfica. Permite al usuario obtener estadísticas como número de palabras, líneas, palabra más frecuente, top N, porcentaje de palabras únicas, y más.

## Características principales

- Entrada de texto manual o desde archivo `.txt`
- Análisis multihilo usando `ThreadPoolExecutor` para mejor rendimiento
- Estadísticas clave del texto (palabras, líneas, palabra más usada)
- Funciones extra:
  - Buscar palabra o conjunto de palabras
  - Palabras que empiezan por un prefijo
  - Longitud media de palabras
  - Porcentaje de palabras únicas
- Interfaz gráfica moderna con `ttkbootstrap`
- Ayuda integrada para usuarios que no conocen cómo encontrar la ruta de su archivo

## Decisiones técnicas

- **Multihilo con ThreadPoolExecutor**: Se eligió por su facilidad de uso y eficiencia en tareas independientes como el procesamiento de fragmentos de texto.
- **Diseño modular**: Cada script tiene una función clara, lo que facilita el mantenimiento y escalado del programa.
- **Interfaz GUI con ttkbootstrap**: Para ofrecer una experiencia moderna y profesional sin complicaciones de configuración.

## Estructura del proyecto

