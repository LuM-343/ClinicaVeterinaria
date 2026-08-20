**JUSTIFICACIÓN TÉCNICA**

Mascotas – JSON (un solo archivo, MASCOTAS.json): 
Se guardan todas juntas porque es la única información que necesitamos ver o buscar completa. JSON es fácil de leer y escribir en Python, y permite cambiar solo un dato (como el estado) sin tener que tocar todo el archivo.

Consultas – JSON (un archivo por mascota): 
El diagnóstico y el tratamiento son texto libre, pueden tener comas o tildes, y eso complica un CSV. JSON no tiene ese problema. Guardar un archivo por mascota hace que cada historial esté separado, sin mezclarse con el de otras.

Vacunas – CSV (un archivo por mascota): 
Los datos de una vacuna son cortos y siempre tienen la misma forma (nombre, fecha, próxima dosis, veterinario), sin texto largo. Por eso CSV alcanza y es más simple, además se puede abrir en Excel para revisarlo a mano.

Documentos – archivos reales + un índice JSON por mascota: 
Las fotos y PDFs son archivos, no se pueden guardar como texto sin complicarlos. Se dejan como archivos normales dentro de la carpeta de cada mascota, y el índice JSON solo anota el nombre, la descripción y la fecha de cada uno.
