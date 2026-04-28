# ✈️ Laboratorio 2 - Grafos de Transporte Aéreo

## 📌 Descripción

Este proyecto implementa un **grafo simple, no dirigido y ponderado** que modela rutas de transporte aéreo entre aeropuertos del mundo.

Cada vértice representa un aeropuerto y cada arista representa una conexión entre dos aeropuertos, cuyo peso corresponde a la **distancia geográfica calculada mediante la fórmula de Haversine**.

El sistema permite analizar propiedades del grafo y ejecutar algoritmos clásicos de teoría de grafos como:

* Conectividad
* Bipartición
* Árbol de expansión mínima (MST)
* Caminos mínimos

---

## 🧠 Objetivos

* Modelar un problema real mediante grafos
* Implementar algoritmos sin uso de librerías externas
* Aplicar estructuras de datos en un contexto práctico
* Visualizar información geográfica de aeropuertos

---

## 📊 Dataset

Se utiliza el archivo:

```
data/flights_final.csv
```

Contiene información de vuelos entre aeropuertos, incluyendo:

* Código del aeropuerto
* Nombre
* Ciudad
* País
* Latitud y longitud

---

## ⚙️ Tecnologías utilizadas

* Python 🐍
* Streamlit (interfaz gráfica)
* Pandas (manejo de datos)

---

## 🏗️ Estructura del proyecto

```
scratch-main/
│
├── app.py                  # Interfaz gráfica (Streamlit)
│
├── core/
│   ├── graph.py            # Construcción del grafo
│   └── algorithms.py       # Algoritmos de grafos
│
├── data/
│   └── flights_final.csv   # Dataset
│
└── README.md
```

---

## 🔍 Funcionalidades

### 1. Conectividad del grafo

* Determina si el grafo es conexo
* Si no lo es:

  * Número de componentes
  * Tamaño de cada componente

---

### 2. Verificación de grafo bipartito

* Determina si el grafo es bipartito
* En caso de múltiples componentes:

  * Evalúa la componente más grande

---

### 3. Árbol de expansión mínima (MST)

* Se calcula usando el algoritmo de **Kruskal**
* Se obtiene el peso total del árbol
* En caso de múltiples componentes:

  * Se calcula el MST de cada una

---

### 4. Información de aeropuertos

Dado un aeropuerto inicial:

* Se muestra su información:

  * Código
  * Nombre
  * Ciudad
  * País
  * Coordenadas

---

### 5. Caminos mínimos

* Se utiliza el algoritmo de **Dijkstra**
* Se pueden:

  * Encontrar los 10 aeropuertos más lejanos (por camino mínimo)
  * Mostrar distancias acumuladas

---

### 6. Ruta entre dos aeropuertos

* Se calcula el camino mínimo entre dos vértices
* Se muestran los aeropuertos intermedios

---

## 📐 Cálculo de distancias

Se utiliza la fórmula de Haversine para calcular la distancia entre dos coordenadas geográficas:

* Permite medir distancias sobre la superficie de la Tierra
* Se usa como peso de las aristas del grafo

---

## ▶️ Cómo ejecutar el proyecto

1. Instalar dependencias:

```bash
pip install streamlit pandas
```

2. Ejecutar la aplicación:

```bash
streamlit run app.py
```

3. Abrir en el navegador:

```
http://localhost:8501
```

---

## ⚠️ Restricciones

* No se utilizaron librerías externas para:

  * Conectividad
  * Caminos mínimos
  * MST
  * Bipartición

Todos los algoritmos fueron implementados manualmente.

---

## 👥 Integrantes

* Ricardo Ramos
* Francisco Cuello
* Keinerth De La Hoz 
  

---

## 🎓 Curso

Estructura de Datos II
Universidad del Norte

---

## 📅 Fecha de entrega

29 de abril de 2026

---

## 💡 Observaciones

Este proyecto permite aplicar conceptos teóricos de grafos a un problema real, integrando estructuras de datos, algoritmos y visualización.

---
