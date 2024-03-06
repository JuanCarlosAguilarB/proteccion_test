from fastapi import APIRouter, Request, HTTPException
from typing import List

from .fibonacci_service import reverse_fibonacci_serie
from app.shared.email_send import send_email_async


router = APIRouter(
    prefix="/fibonacci",
    tags=["fibonacci"],
)


@router.get("/")
async def get_fibonacci_serie(request: Request):
    """
    Endpoint to generate and return the Fibonacci series based on Colombian time.

    Returns:
    - dict: A dictionary containing the Colombian time and the Fibonacci series.

    Raises:
    - HTTPException: If there is an error with the initial data or sending the email.
    """
    current_time_colombia = request.state.current_time_colombia

    # Formatear la hora colombiana como string
    formatted_time = current_time_colombia.strftime("%H:%M:%S")

    minute = current_time_colombia.minute
    seconds = current_time_colombia.second

    seed1 = minute // 10
    seed2 = minute % 10 if minute > 10 else minute

    length_serie_fibonacci = seconds

    try:
        serie_fibonaci = reverse_fibonacci_serie(
            seed1, seed2, length_serie_fibonacci)
    except ValueError as e:
        raise HTTPException(
            status_code=500, detail=f"Error con los datos iniciales: {e}")

    await send_email_fibonaci_serie(formatted_time, serie_fibonaci)

    return {"hora_colombiana": formatted_time, "serie_fibonaci": serie_fibonaci}


async def send_email_fibonaci_serie(current_time_colombia: str, serie_fibonaci: List):
    """
    Asynchronously sends an email containing the Fibonacci series and other details.

    Args:
    - current_time_colombia: The current time in the Colombian timezone.
    - serie_fibonaci: The Fibonacci series to include in the email.

    Returns:
    - None

    Raises:
    - None
    """

    body = f"""Hola, muy buen día a todos. \n\n

    La serie de Fibonacci hasta el término dada para la hora: {current_time_colombia} es: \n
    {serie_fibonaci}. \n\n

    url de la documentación: https://54.224.204.103:8000/docs \n

    url del servidor o despliegue en internet: https://54.224.204.103:8000 \n
    
    url del postman https://www.postman.com/joint-operations-geoscientist-20795163/workspace/protecciontest/collection/23108580-339d5254-e595-4237-b0f0-a2ea79057e12?action=share&creator=23108580
    
    """

    list_recipients = ["abjuancarlos.12@gmail.com",
                       "abjuancarlos.12@gmail.com",
                       #    "didier.correa@proteccion.com.co",
                       #    "correalondon@gmail.com"
                       ]

    await send_email_async("Prueba Técnica - Juan Carlos Aguilar Bosiga",
                           list_recipients, body)
