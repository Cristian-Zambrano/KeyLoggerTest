# 🛠️ Prueba de Keylogger Básico con Envío de Correo ✉️

Este proyecto es una **prueba de concepto** de un keylogger básico que, al detectar ciertas teclas (como `Enter` o `Tab`), envía un correo con la información capturada por el programa.  
Está pensado exclusivamente para fines educativos y demostraciones técnicas.

---

## ⚙️ Requisitos y Configuración

### 📦 1. Instalar dependencias

Ejecuta el siguiente comando en tu terminal para instalar los paquetes necesarios:

```bash
pip install -r .\requirements.txt
```
### 🦅 2. Crea tu archivo .env
Define tus credenciales de correo y configuración SMTP en un archivo .env ubicado en la raíz del proyecto:
EMAIL_USER=tuemail@gmail.com
EMAIL_PASSWORD=tu_contraseña_segura
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=465
EMAIL_FROM_NAME=Keylogger Prueba
EMAIL_DEFAULT_RECEIVER=destinatario@ejemplo.com
### 🚀 3. Cómo Funciona
- Escucha pulsaciones de teclas en segundo plano.
- Cuando detecta Enter o Tab, dispara el envío de un correo con la información capturada.

Si se configura un archivo adjunto, también lo incluye.
## 🔒 Asegúrate de no subir este archivo al repositorio. Ya está ignorado mediante .gitignore.
## ⚠️ Advertencia
Este código es únicamente para fines educativos y de evaluación supervisada.
🚫 No debe utilizarse con fines maliciosos o sin el consentimiento explícito del usuario objetivo.

## 🧑‍🏫 Nota para el Profesor
Por motivos de seguridad y siguiendo buenas prácticas de desarrollo:
🔐 El archivo .env no ha sido incluido en este repositorio. Esto evita la exposición de credenciales sensibles y garantiza el cumplimiento de estándares éticos en el manejo de software potencialmente sensible.

## Elaborado por: Cristian Zambrano
## Referencia: https://www.youtube.com/watch?v=mDY3v2Xx-Q4
