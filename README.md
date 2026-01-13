# 🎬 Flet Películas App

Aplicación de escritorio desarrollada con **Python + Flet**, que implementa un **CRUD completo de películas**, conexión a base de datos con **SQLAlchemy**, variables de entorno con **dotenv** y empaquetado final como **archivo ejecutable (.exe)** usando **PyInstaller**.

Este proyecto está pensado como **guía práctica de aprendizaje**, desde la creación del entorno virtual hasta la distribución final de una aplicación de escritorio profesional.

---

## 🚀 Tecnologías utilizadas

* **Python 3.12+**
* **Flet** – Framework para aplicaciones de escritorio/web
* **SQLAlchemy** – ORM para base de datos
* **MySQL** (vía PyMySQL)
* **python-dotenv** – Manejo de variables de entorno
* **PyInstaller** – Empaquetado a `.exe`
* **PowerShell 7** / **PyCharm**

---

## 📂 Estructura del proyecto

```
flet_peliculas/
│
├── app.py                  # Punto de entrada principal
├── database.py             # Configuración de la base de datos
├── models/
│   ├── __init__.py
│   └── pelicula.py         # Modelo SQLAlchemy
│
├── services/
│   ├── __init__.py
│   └── pelicula_service.py # Lógica CRUD
│
├── views/
│   ├── __init__.py
│   ├── home_view.py        # Vista principal
│   └── form_view.py        # Formulario de películas
│
├── .env                    # Variables de entorno (NO subir a GitHub)
├── requirements.txt
├── .venv/                  # Entorno virtual
└── README.md
```

---

## ⚙️ Configuración inicial

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/flet-peliculas.git
cd flet-peliculas
```

---

### 2️⃣ Crear y activar entorno virtual

**PowerShell (Windows):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 3️⃣ Instalar dependencias

```powershell
pip install -r requirements.txt
```

Si no tienes el archivo:

```powershell
pip install flet sqlalchemy pymysql python-dotenv pyinstaller
```

---

## 🗄️ Variables de entorno (.env)

Crea un archivo `.env` en la raíz del proyecto:

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=peliculas_db
```

⚠️ **Nunca subas este archivo a GitHub**

---

## ▶️ Ejecutar la aplicación

```powershell
python app.py
```

La aplicación se abrirá como **ventana de escritorio** usando Flet.

---

## 🧠 Conceptos clave aprendidos

* Arquitectura por capas (views, services, models)
* Manejo correcto de imports en Python
* Uso de `__init__.py`
* Conexión a base de datos con SQLAlchemy
* Manejo de errores comunes en Flet
* Empaquetado real a `.exe`
* Solución de dependencias faltantes en PyInstaller

---

## 📦 Empaquetar como archivo .exe

### Comando recomendado

```powershell
pyinstaller --clean --noconsole --onefile app.py
```

📁 El ejecutable se genera en:

```
dist/app.exe
```

---

### Evitar falsos positivos de antivirus

```powershell
pyinstaller --clean --noconsole --onefile --noupx --name FletPeliculas app.py
```

---

## ❗ Errores comunes y soluciones

### ❌ `ModuleNotFoundError`

✔ Asegúrate de instalar las dependencias dentro del `.venv`

```powershell
pip install nombre_paquete
```

---

### ❌ El `.exe` no abre pero en PyCharm sí

✔ Faltaban dependencias como:

* `pymysql`
* `sqlalchemy`
* `dotenv`

✔ Solución:

```powershell
pip install pymysql sqlalchemy python-dotenv
```

---

## 📌 Recomendaciones finales

* Usa siempre entorno virtual
* No mezcles PowerShell con Bash
* Mantén imports relativos claros
* Documenta tu proyecto (como este README 😉)

---

## 🙌 Autor

**Eduardo V.**
Proyecto educativo – aprendizaje práctico de Flet + Python

---

⭐ Si este proyecto te ayudó, ¡dale una estrella en GitHub!
