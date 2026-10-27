# GCI World 2026 — Data Science & Machine Learning

Coursework and projects completed in **GCI World 2026** (University of Tokyo): Python for data analysis, a machine learning competition, and graded homework.

🎓 **Certificate:** [add link to your certificate or verification page]

> 🇪🇸 Versión en español más abajo.

---

## What's in this repo

| Folder | What it is | Skills |
|---|---|---|
| [`homework/`](./homework) | Three graded homework assignments (Sessions 2–4) | NumPy, Pandas |
| [`nfl-draft-prediction/`](./nfl-draft-prediction) | Machine learning competition: predict which college players get drafted | Classification, scikit-learn, ROC-AUC |
| [`final-assignment/`](./final-assignment) | *(Delete this row if you did not submit one.)* Business proposal based on data analysis and an ML model | EDA, modeling, business communication |

---

## 🏈 NFL Draft Prediction (ML competition)

**Goal:** predict whether a college football player will be selected in the NFL Draft, using physical performance tests and body measurements.

- **Target:** `Drafted` (1 = selected, 0 = not selected). The model outputs a probability between 0 and 1.
- **Metric:** ROC-AUC.
- **Data:** the training and test files provided by the competition. No external data was used.

**My approach**

- **Features:** [e.g. height, weight, 40-yard dash, vertical jump, bench press, broad jump, agility drills, position]
- **Preprocessing:** [e.g. how you handled missing values, categorical encoding]
- **Model:** [e.g. Random Forest / Gradient Boosting / Logistic Regression]
- **Validation:** [e.g. 5-fold cross-validation]
- **Result:** [your AUC score]. [Leaderboard position, if you want to include it.]

**What I learned:** [1–2 sentences: what worked, what did not, what you would try next.]

**Reproducibility:** random seeds are fixed (`random_state = [your seed]`), so the notebook gives the same results when re-run.

---

## 📚 Homework

| # | Topic | What I practiced |
|---|---|---|
| 1 | Filtering a NumPy array with boolean masks (multiples of 5 that are odd) | Vectorized operations, boolean indexing |
| 2 | Average score per category on an anime dataset | Pandas `groupby`, aggregation, sorting |
| 3 | Concentration (Pareto / 80-20) analysis by deciles | `rank`, `qcut`, proportions of a total |

Each notebook includes the problem statement and my solution.

---

## 🧰 Tech stack

Python · NumPy · Pandas · Matplotlib · scikit-learn · Jupyter / Google Colab

## ▶️ How to run

```bash
git clone https://github.com/DanielaM1293/[repo-name].git
cd [repo-name]
pip install -r requirements.txt
jupyter notebook
```

**Data:** the competition and course datasets are not included in this repo. [Add where to download them, or how to get them from the course platform.]

## 🤖 AI use

[Be honest and specific, for example: "I used an AI assistant to understand error messages and review my code; the modeling decisions and final notebooks are my own." If you used none, say so.]

---

## 👩‍💻 Author

**Estefany Martínez** — Junior Frontend / Full-Stack Developer · Bogotá, Colombia
[GitHub](https://github.com/DanielaM1293) · [LinkedIn](https://www.linkedin.com/in/estefany-daniela-mart%C3%ADnez-ni%C3%B1o-b0832b209) · [Portfolio](https://estefanymar.netlify.app)

---

# 🇪🇸 Versión en español

## GCI World 2026 — Ciencia de Datos y Machine Learning

Trabajos y proyectos del curso **GCI World 2026** (Universidad de Tokio): Python para análisis de datos, una competencia de machine learning y tareas calificadas.

🎓 **Certificado:** [agrega el enlace a tu certificado]

### Contenido

| Carpeta | Qué es | Habilidades |
|---|---|---|
| [`homework/`](./homework) | Tres tareas calificadas (Sesiones 2–4) | NumPy, Pandas |
| [`nfl-draft-prediction/`](./nfl-draft-prediction) | Competencia de ML: predecir qué jugadores universitarios serán seleccionados en el draft de la NFL | Clasificación, scikit-learn, ROC-AUC |
| [`final-assignment/`](./final-assignment) | *(Borra esta fila si no entregaste uno.)* Propuesta de negocio basada en análisis de datos y un modelo de ML | EDA, modelado, comunicación de negocio |

### 🏈 Predicción del NFL Draft

- **Objetivo:** predecir si un jugador será seleccionado, a partir de pruebas físicas y medidas corporales.
- **Variable objetivo:** `Drafted` (1 = seleccionado, 0 = no). El modelo entrega una probabilidad entre 0 y 1.
- **Métrica:** ROC-AUC. No se usaron datos externos.
- **Enfoque:** [variables, preprocesamiento, modelo y validación]
- **Resultado:** [tu AUC]
- **Reproducibilidad:** semillas fijadas (`random_state = [tu semilla]`).

### 📚 Tareas

1. Filtrado de un arreglo NumPy con máscaras booleanas.
2. Promedio de puntaje por categoría con Pandas (`groupby`).
3. Análisis de concentración (Pareto / 80-20) por deciles.

### ▶️ Cómo ejecutarlo

Instala las dependencias con `pip install -r requirements.txt` y abre los notebooks con Jupyter o Google Colab. Los datasets no están incluidos en este repo. [Indica dónde descargarlos.]

### 🤖 Uso de IA

[Cuéntalo con honestidad, por ejemplo: "Usé un asistente de IA para entender errores y revisar mi código; las decisiones de modelado y los notebooks finales son míos."]
