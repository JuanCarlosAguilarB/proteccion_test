from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List


def email_config():

    # Configurar el servidor SMTP y enviar el correo electrónico
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('projects.devs101@gmail.com', 'nsfcqqmrwhstfylu')

        return smtp_server

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"No se pudo enviar configurar el servidor  de correo electrónico: {e}")


async def send_email_async(subject: str, email_to: List[str], body: dict):
    try:
        smtp_server = email_config()

        msg = MIMEMultipart()
        msg['From'] = 'projects.devs101@gmail.com'
        msg['To'] = ", ".join(email_to)
        msg['Subject'] = subject

        # body = f"La serie de Fibonacci hasta el término {n} es: {fibonacci_series}"
        msg.attach(MIMEText(body, 'plain'))

        smtp_server.send_message(msg)
        smtp_server.quit()

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"No se pudo enviar el correo electrónico: {e}")
