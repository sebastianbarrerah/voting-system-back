
# 🗳️ Sistema de Votaciones con FastAPI y PostgreSQL

Este proyecto es una API REST que permite registrar votantes y obtener sus datos, utilizando FastAPI y PostgreSQL como base de datos.

---

## 🧰 Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python 3.8+
- PostgreSQL
- pip (gestor de paquetes de Python)
- Git 

---

## 📝 Pasos para correr el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sistema-votaciones.git
cd sistema-votaciones
pip install -r requirements.txt
```
**2. Archivo Copy .env** 
Se crea un archivo .env con los datos que hay el copy, se añade URI de conexión personal (En este proyecto no es necesario la uri es publica) y se corre el proyecto.
**3 Correr el proyecto**

    uvicorn app.main:app --reload

**4 Mirar documentación**
***swagger:*** http://localhost:8000

**5 Front**
https://github.com/sebastianbarrerah/prueba-tecnica-front/tree/main
