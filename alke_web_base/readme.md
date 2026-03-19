# Alke Wallet 💳

Aplicación web de billetera digital desarrollada con **Python** y **Django** como proyecto del Módulo 6 del curso de Desarrollo de Aplicaciones Web con Python Django.

---

## Descripción

Alke Wallet es una simulación de billetera digital que permite a los usuarios gestionar su cuenta, depositar dinero, enviar transferencias a contactos y consultar el historial de movimientos. Todo el estado de la sesión se maneja del lado del servidor mediante las sesiones de Django, sin necesidad de base de datos persistente para los datos de usuario.

---

## Funcionalidades

| Módulo | Descripción |
|---|---|
| **Login** | Autenticación de usuario con credenciales fijas de prueba |
| **Menú principal** | Vista del saldo actual y acceso rápido a todas las secciones |
| **Depositar** | Incrementa el saldo de la cuenta y registra el movimiento |
| **Enviar dinero** | Transferencia a contactos de la lista, con validación de saldo |
| **Agregar contacto** | Alta de nuevos destinatarios (nombre, CBU, alias, banco, correo) |
| **Transacciones** | Historial cronológico de depósitos y envíos realizados |

---

## Tecnologías

- **Python 3.x**
- **Django 6.0.3**
- **SQLite 3** (base de datos por defecto)
- **HTML5 / CSS3 / JavaScript** (frontend sin frameworks adicionales)
- **Bootstrap Icons** (iconografía en la interfaz)

---

## Estructura del proyecto
alke_web_base/
├── manage.py
├── db.sqlite3
├── alke_solutions/ # Configuración principal del proyecto Django
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── web_base/ # Aplicación principal
│ ├── views.py # Lógica de todas las vistas
│ ├── urls.py # Rutas de la aplicación
│ ├── models.py
│ ├── admin.py
│ └── templates/ # Plantillas HTML
│ ├── base.html
│ ├── login.html
│ ├── menu.html
│ ├── deposit.html
│ ├── sendmoney.html
│ └── transactions.html
├── static/
│ ├── css/ # Hojas de estilo por módulo
│ │ ├── styles.css # Estilos globales y layout
│ │ ├── login.css
│ │ ├── menu.css
│ │ ├── deposit.css
│ │ └── transactions.css
│ └── javascript/ # Scripts por módulo
│ ├── login.js
│ ├── menu.js
│ ├── deposit.js
│ ├── sendmoney.js
│ ├── transactions.js
│ └── utils.js
└── env/ # Entorno virtual Python
---

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd alke_web_base

### 2. Crear y activar el entorno virtual

python -m venv env

# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate

### 3. Instalar dependencias

pip install django==6.0.3

### 4. Aplicar migraciones

python manage.py migrate

### 5. Iniciar el servidor de desarrollo

python manage.py runserver

La aplicación estará disponible en http://127.0.0.1:8000/.

### Credenciales de acceso (demo)

Campo	Valor
Correo	correo@correo.com
Contraseña	12345

⚠️ Estas credenciales son fijas y solo sirven para propósitos de demostración.

Rutas disponibles
URL	Vista	Descripción
/	login_view	Página de inicio de sesión
/menu/	menu_view	Panel principal del usuario
/deposit/	deposit_view	Formulario de depósito
/send-money/	send_money_view	Envío de dinero a contactos
/add-contact/	add_contact_view	Alta de nuevo contacto
/transactions/	transactions_view	Historial de movimientos
Notas
El proyecto usa DEBUG = True. No usar en producción sin configurar correctamente ALLOWED_HOSTS y cambiar la SECRET_KEY.
El saldo y los movimientos se almacenan en la sesión de Django y se reinician al cerrar sesión o borrar la cookie de sesión.
No se requiere superusuario de Django para utilizar la aplicación.

Autor Constanza Fernanda Saa Mercado

Desarrollado como proyecto final del Módulo 6 — Desarrollo de Aplicaciones Web con Python Django.