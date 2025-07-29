# Estructura de Plantillas del Blog SonarHoy

Esta documentación resume cómo están organizadas las plantillas HTML del proyecto **SonarHoy**, y cómo se reutilizan en las diferentes aplicaciones del sistema (por ejemplo: `user`, `post`, etc).

---

## 📁 Estructura de Archivos

La estructura de templates se encuentra bajo:

```
blog/templates/
├── layout.html        # Plantilla base principal
├── header.html        # Encabezado con banner, redes, nav y modo oscuro
├── footer.html        # Pie de página con redes, enlaces y logo
├── estado.html        # Plantilla hija de ejemplo con contenido dinámico
```

---

## 📌 layout.html

Archivo base general. Define la estructura principal del sitio:

- Incluye estilos generales (inputs y modo oscuro)
- Carga `header.html` y `footer.html`
- Contiene el bloque `{% block content %}` para cargar contenido dinámico

Ejemplo de uso en una app:

```django
{% extends 'layout.html' %}

{% block title %}Título de la página{% endblock %}

{% block content %}
  <h1>Contenido específico de esta vista</h1>
{% endblock %}
```

---

## 🔗 header.html

Incluido en `layout.html`. Contiene:

- Banner principal con logo grande (`Marca_1.png`)
- Barra superior con redes sociales
- Control de modo oscuro con persistencia (`localStorage`)
- Barra de búsqueda
- Navegación principal (Noticias, Agenda, Contacto, Quienes somos)
- Botones de login/registro o perfil, dependiendo del contexto (`title`)

---

## 🔗 footer.html

Incluido en `layout.html`. Contiene:

- Iconos de redes sociales
- Enlaces rápidos
- Logo de SonarHoy y derechos reservados

---

## 🧱 Cómo usarlo en otras aplicaciones

### App: `user`

Templates como `login.html`, `register.html`, `profile.html` deben extender `layout.html`:

```django
{% extends 'layout.html' %}

{% block title %}Iniciar sesión{% endblock %}

{% block content %}
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
  </form>
{% endblock %}
```

---

### App: `post`

Los templates de publicaciones como `post_list.html`, `post_detail.html` también usan `layout.html`:

```django
{% extends 'layout.html' %}

{% block title %}Últimas publicaciones{% endblock %}

{% block content %}
  {% for post in posts %}
    <h2>{{ post.titulo }}</h2>
    <p>{{ post.contenido|truncatewords:30 }}</p>
    <a href="{% url 'post:detalle' post.slug %}">Leer más</a>
  {% endfor %}
{% endblock %}
```

---

## ✅ Ventajas de esta estructura

- Evita duplicar código (DRY)
- Facilita mantener el diseño en todas las apps
- Es modular y extensible (se pueden crear más includes)
- Permite estilos consistentes y personalización por app

---



© 2025 SonarHoy. Documentación interna de estructura de plantillas.