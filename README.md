🌟 SonarHoy

SonarHoy es una plataforma web de noticias y agendas desarrollada en Django y Tailwind CSS, que permite publicar contenido, interactuar mediante comentarios y "likes", y gestionar perfiles de usuario de forma segura y moderna.

---

🚀 Características

- Gestión de publicaciones: Crear, editar y eliminar posts con imágenes y categorías.
- Sistema de comentarios: Comentarios inline con opción de edición y eliminación.
- Likes en posts: Los usuarios pueden dar "Me gusta" a las publicaciones.
- Perfiles de usuario: Registro, login, acceso de invitados, avatar editable y roles diferenciados.
- Tema claro/oscuro: Toggle persistente que recuerda la preferencia del usuario.
- Diseño responsivo: Adaptado a celulares y tablets mediante Tailwind CSS.
- Seguridad y permisos: Solo administradores o usuarios con permisos pueden crear publicaciones.

---

🛠 Tecnologías

- Backend: Django 5.2+
- Frontend: HTML5, Tailwind CSS, JavaScript
- Base de datos: SQLite / PostgreSQL (configurable)
- Control de versiones: Git & GitHub
- Dependencias y entorno: Python 3.12+, Pipenv

---

📂 Estructura del proyecto

SonarHoy/
├─ blog/
│  ├─ apps/
│  │  ├─ user/          # Autenticación y perfiles
│  │  ├─ post/          # Publicaciones y categorías
│  │  └─ contacto_admin/ # Mensajes y administración
│  └─ templates/
│     ├─ layout.html     # Layout base
│     ├─ header.html
│     └─ footer.html
├─ static/              # Imágenes, CSS, JS
├─ Pipfile
├─ .env.example
└─ manage.py

---

⚡ Instalación

1. Clonar el repositorio:
git clone https://github.com/AlexiasXro/SonarHoy.git
cd SonarHoy

2. Crear e ingresar al entorno virtual:
pipenv shell

3. Instalar dependencias:
pipenv install

4. Configurar variables de entorno:
cp .env.example .env

5. Migrar la base de datos:
python manage.py migrate

6. Ejecutar el servidor:
python manage.py runserver

7. Acceder a la app en http://127.0.0.1:8000/.

---

👥 Participantes

Nombre                        | Rol                                                                                                            | GitHub
-------------------------------|--------------------------------                                                                               |-------------------------------
Alejandra Romina Cáceres       | Repo principal en GitHub, definición y desarrollo de DER, Backend (user y layout), Digital Project Manager    | https://github.com/AlexiasXro
Flor Azcoaga                   | Definición de criterios de aceptación, Backend y Frontend (home, agenda, contacto y quienes somos), Diseño UI | https://github.com/xikiotaka
Nahuel Storace                 | Desarrollador Frontend (user, header, footer, layout)                                                         | https://github.com/Nahuel-srce
Martina Kendrick               | Desarrolladora Backend (post)                                                                                 | https://github.com/MartinaKndk
Ezequiel Ávalos                | Desarrollador Frontend (post)                                                                                 | https://github.com/EzeAvalos25

---

🌐 Contacto

- Instagram: https://www.instagram.com/carpinchosg2/

¡Gracias por contribuir a SonarHoy! 🚀


## 📚 Documentación de Plantillas

Ver documentación de plantillas base:  
[📄 plantillas.md](/docs/plantillas.md)

Ver documentación perfil:  
[📄 plantillas.md](/docs/perfil_usuario.md)
