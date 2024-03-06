from fastapi import APIRouter, Request
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

    """
    current_time_colombia = request.state.current_time_colombia

    # Formatear la hora colombiana como string
    formatted_time = current_time_colombia.strftime("%H:%M:%S")

    minute = current_time_colombia.minute
    seconds = current_time_colombia.second

    seed1 = minute // 10
    seed2 = minute % 10 if minute > 10 else minute

    length_serie_fibonacci = seconds

    print(minute, seconds)
    print(seed1, seed2, length_serie_fibonacci)

    serie_fibonaci = reverse_fibonacci_serie(
        seed1, seed2, length_serie_fibonacci)

    await send_email_fibonaci_serie(formatted_time, serie_fibonaci)

    return {"hora_colombiana": formatted_time, "serie_fibonaci": serie_fibonaci}


async def send_email_fibonaci_serie(current_time_colombia: str, serie_fibonaci: List):

    body = f"""Hola, muy buen día a todos. \n\n

    La serie de Fibonacci hasta el término dada para la hora: {current_time_colombia} es: \n
    {serie_fibonaci}

    """

    list_recipients = ["abjuancarlos.12@gmail.com",
                       "abjuancarlos.12@gmail.com",
                       #    "didier.correa@proteccion.com.co",
                       #    "correalondon@gmail.com"
                       ]

    await send_email_async("Prueba Técnica - Juan Carlos Aguilar Bosiga",
                           list_recipients, body)
