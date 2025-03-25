# Esta es una interfaz moderna paea acompañar el código



# NOTA: ES MUY IMPORTANTE QUE CUANDO SE EJECUTE LA INTERFAZ SE AMPLÍEN LAS PESTAÑAS, LOS BOTONES ESTARÁN OCULTOS




import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from tkinter import filedialog, messagebox, simpledialog
from procesamiento import procesar_texto_en_hilos, contar_lista_palabras, longitud_media_palabras, porcentaje_palabras_unicas
import os


class AnalizadorTextoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Analizador de Texto Multihilo")
        self.root.geometry("800x650")

        self.texto = ""
        self.resultado = None

        self.crear_widgets()

    def crear_widgets(self):
        titulo = ttk.Label(self.root, text="📥 Bienvenido al Analizador de Texto", font=("Segoe UI", 16, "bold"))
        titulo.pack(pady=10)

        boton_cargar = ttk.Button(self.root, text="📂 Cargar archivo .txt", command=self.opcion_cargar_archivo, bootstyle=SUCCESS)
        boton_cargar.pack(pady=5)

        separator = ttk.Label(self.root, text="o")
        separator.pack()

        boton_manual = ttk.Button(self.root, text="✍️ Introducir texto manualmente", command=self.introducir_manual, bootstyle=PRIMARY)
        boton_manual.pack(pady=5)

        self.resultados = ScrolledText(self.root, wrap='word', width=90, height=20, font=("Consolas", 10))
        self.resultados.pack(pady=15)

        self.boton_menu_extra = ttk.Button(self.root, text="🔧 Abrir menú de funciones extra", command=self.mostrar_menu_opciones_extra, bootstyle=WARNING)
        self.boton_menu_extra.pack(pady=5)
        self.boton_menu_extra.config(state='disabled')

    def opcion_cargar_archivo(self):
        respuesta = messagebox.askyesno("Ayuda", "¿Necesitas ayuda para encontrar la ruta del archivo?")
        if respuesta:
            self.mostrar_ayuda_ruta()
        self.cargar_archivo()

    def mostrar_ayuda_ruta(self):
        ayuda = """📁 Para encontrar la ruta del archivo:

🪟 En Windows:
1. Abre la carpeta del archivo
2. Clic derecho → Propiedades
3. Copia la ruta y añade \\nombre_del_archivo.txt

🐧 En Mac/Linux:
1. Abre la carpeta del archivo
2. Clic derecho → Obtener información
3. Copia la ruta y añade /nombre_del_archivo.txt
"""
        messagebox.showinfo("Ayuda para obtener la ruta", ayuda)

    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    self.texto = archivo.read()
                    self.mostrar_resultados()
            except Exception as e:
                messagebox.showerror("Error", f"❌ No se pudo leer el archivo:\n{e}")

    def introducir_manual(self):
        ventana_manual = ttk.Toplevel(self.root)
        ventana_manual.title("📝 Introducir texto")
        ventana_manual.geometry("550x500")

        contenedor = ttk.Frame(ventana_manual)
        contenedor.pack(fill='both', expand=True, padx=10, pady=10)

        instrucciones = ttk.Label(contenedor, text="✍️ Escribe tu texto abajo.\nCuando termines, pulsa el botón para analizar.", font=("Segoe UI", 10))
        instrucciones.pack(pady=5)

        text_area = ScrolledText(contenedor, wrap='word', width=60, height=18, font=("Consolas", 10))
        text_area.pack(pady=5)

        def guardar_texto():
            self.texto = text_area.get("1.0", 'end').strip()
            if self.texto:
                self.mostrar_resultados()
                ventana_manual.destroy()
            else:
                messagebox.showwarning("Texto vacío", "⚠️ Por favor, escribe algún texto.")

        boton_guardar = ttk.Button(contenedor, text="✨ Finalizar y analizar texto", command=guardar_texto, bootstyle=SUCCESS)
        boton_guardar.pack(pady=10)

    def mostrar_resultados(self):
        self.resultado = procesar_texto_en_hilos(self.texto, num_hilos=4)

        resumen = f"\n📊 Resultados del análisis:\n"
        resumen += f"\n🔢 Total de palabras: {self.resultado['num_total_palabras']}"
        resumen += f"\n📈 Total de líneas: {self.resultado['num_total_lineas']}"
        resumen += f"\n🏆 Palabra más frecuente: '{self.resultado['palabra_mas_frecuente'][0]}' ({self.resultado['palabra_mas_frecuente'][1]} veces)\n"

        resumen += "\n📌 Top 10 palabras más frecuentes:\n"
        for palabra, cuenta in self.resultado['contador_total'].most_common(10):
            resumen += f"   🔹 {palabra}: {cuenta} veces\n"

        self.resultados.delete("1.0", 'end')
        self.resultados.insert('end', resumen)
        self.boton_menu_extra.config(state='normal')

    def mostrar_menu_opciones_extra(self):
        if not self.resultado:
            messagebox.showwarning("Advertencia", "⚠️ Primero debes analizar un texto.")
            return

        contador_total = self.resultado['contador_total']

        ventana_menu = ttk.Toplevel(self.root)
        ventana_menu.title("🔧 Funciones Extra")
        ventana_menu.geometry("500x400")

        opciones = [
            ("🔍 Buscar palabra", lambda: self.buscar_palabra(contador_total)),
            ("🏅 Top N palabras", lambda: self.top_n(contador_total)),
            ("🔡 Palabras por prefijo", lambda: self.palabras_por_prefijo(contador_total)),
            ("📏 Longitud media", lambda: self.longitud_media(contador_total)),
            ("🧠 % Palabras únicas", lambda: self.porcentaje_unicas(contador_total)),
        ]

        for texto, accion in opciones:
            boton = ttk.Button(ventana_menu, text=texto, command=accion, bootstyle=SECONDARY)
            boton.pack(pady=5)

    def buscar_palabra(self, contador):
        palabra = simpledialog.askstring("Buscar palabra", "🔍 Escribe la palabra a buscar:")
        if palabra:
            conteo = contador[palabra]
            messagebox.showinfo("Resultado", f"✅ La palabra '{palabra}' aparece {conteo} veces.")

    def top_n(self, contador):
        try:
            n = simpledialog.askinteger("Top N", "🏅 ¿Cuántas palabras quieres ver?")
            if n:
                top = contador.most_common(n)
                resultado = "\n".join([f"🔹 {p}: {c} veces" for p, c in top])
                messagebox.showinfo("Top N", resultado)
        except:
            pass

    def palabras_por_prefijo(self, contador):
        prefijo = simpledialog.askstring("Prefijo", "🔡 Escribe una letra o prefijo:")
        if prefijo:
            coincidencias = {p: c for p, c in contador.items() if p.lower().startswith(prefijo.lower())}
            if coincidencias:
                resultado = "\n".join([f"🔸 {p}: {c} veces" for p, c in coincidencias.items()])
                messagebox.showinfo("Coincidencias", resultado)
            else:
                messagebox.showinfo("Coincidencias", "😕 No se encontraron palabras con ese prefijo.")

    def longitud_media(self, contador):
        media = longitud_media_palabras(contador)
        messagebox.showinfo("Longitud media", f"📏 Longitud media de palabras: {media:.2f} letras")

    def porcentaje_unicas(self, contador):
        porcentaje = porcentaje_palabras_unicas(contador)
        messagebox.showinfo("Únicas", f"🧠 Porcentaje de palabras únicas: {porcentaje:.2f}%")


if __name__ == "__main__":
    app = ttk.Window(themename="flatly")
    AnalizadorTextoApp(app)
    app.mainloop()
