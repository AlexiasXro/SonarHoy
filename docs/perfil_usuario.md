# Módulo de Perfil de Usuario - SonarHoy

Este módulo permite a los usuarios registrados gestionar su información personal desde una interfaz centralizada.

---

## ✅ Funcionalidades implementadas

- Vista `ProfileView` basada en `UpdateView`, accesible solo para usuarios autenticados.
- Edición de campos: `first_name`, `last_name`, `email`.
- Carga y actualización de imagen de perfil (`avatar`) mediante un formulario separado.
- Validación combinada (`user_form` + `avatar_form`) en el mismo template.
- Persistencia y visualización del avatar con `MEDIA_URL`.
- Visualización del avatar y nombre del usuario en:
  - Página de perfil.
  - Navbar o sidebar del sitio (ya integrado).

---

## 📁 Archivos relacionados

- `views.py`: clase `ProfileView`
- `models.py`: modelo `Profile` con campo `avatar`
- `forms.py`: `ProfileAvatarForm` (formulario de imagen)
- `templates/user/profile.html`: template principal del perfil
- `templates/components/avatar.html`: componente para mostrar avatar

---

## 🔒 Acceso

Ruta protegida: `/user/profile/`  
Solo accesible para usuarios autenticados (`LoginRequiredMixin`).

---

## ✍️ Notas

- En desarrollo, `MEDIA_URL` y `MEDIA_ROOT` deben estar configurados.
- En producción, debe configurarse un servidor de archivos estáticos/media (como NGINX o S3).
