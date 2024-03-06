from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import pytz


class ColombiaTimeZoneMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        colombia_timezone = pytz.timezone('America/Bogota')

        # Obtener la hora actual en UTC
        current_time_utc = datetime.utcnow()

        # Convertir la hora actual a la zona horaria colombiana
        current_time_colombia = current_time_utc.astimezone(colombia_timezone)

        # Agregar la hora colombiana al estado de la solicitud
        request.state.current_time_colombia = current_time_colombia

        response = await call_next(request)
        return response
