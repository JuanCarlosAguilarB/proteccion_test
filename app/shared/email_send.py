from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List


def email_config():
    """
    Configure the SMTP server and login to send email.

    Returns:
    - smtp_server: Configured SMTP server object.
    """
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('projects.devs101@gmail.com', 'nsfcqqmrwhstfylu')

        return smtp_server

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to configure email server: {e}")


async def send_email_async(subject: str, email_to: List[str], body: str):
    """
    Send an email asynchronously.

    Args:
    - subject: Subject of the email.
    - email_to: List of email addresses to send the email to.
    - body: Body of the email.

    Raises:
    - HTTPException: If sending the email fails.
    """
    try:
        smtp_server = email_config()

        msg = MIMEMultipart()
        msg['From'] = 'projects.devs101@gmail.com'
        msg['To'] = ", ".join(email_to)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        smtp_server.send_message(msg)
        smtp_server.quit()

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to send email: {e}")
