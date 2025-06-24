
# 🧬 Comparación genómica con FastANI y Skani

Este proyecto permite realizar comparaciones de genomas utilizando dos herramientas de ANI (Average Nucleotide Identity):

- `FastANI`: Comparación rápida de pares de genomas.
- `Skani`: Generación de matriz triangular para visualización.

---

## 📁 Estructura esperada

El script asume que los genomas están almacenados como archivos `.fna` descomprimidos dentro de la carpeta:

```
genomic/
```

---

## ⚙️ Script: `comparar_genomas.sh`

Este script realiza las siguientes tareas automáticamente:

1. 📦 Descomprime archivos `.fna.gz` si existen.
2. 📄 Genera una lista de archivos `.fna`.
3. 🧠 Ejecuta `skani triangle` para generar una matriz de comparación.
4. 🧠 Ejecuta `fastANI` para comparar todos los genomas contra todos.

---

## ▶️ Uso

Haz el script ejecutable y ejecútalo:

```bash
chmod +x comparar_genomas.sh
./comparar_genomas.sh
```

---

## ✅ Requisitos

Asegúrate de tener instaladas las siguientes herramientas en tu sistema:

- `skani`
- `fastANI`
- `gzip` (para descomprimir si es necesario)

---

## 🧾 Archivos generados

- `genome_list.txt`: Lista de genomas `.fna` incluidos.
- `skani_output.tsv`: Matriz de ANI generada por Skani.
- `fastani_output.tsv`: Comparaciones uno a uno generadas por FastANI.

---

## 🧠 Autor

Francisco Astorga, automatizado con ❤️ por ChatGPT.
