from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import pytz


class ColombiaTimeZoneMiddleware(BaseHTTPMiddleware):
    """
    Middleware to set the current time in the Colombia timezone for each request.
    """
    async def dispatch(self, request, call_next):
        """
        Dispatch method to set the current time in the Colombia timezone for each request.

        Args:
        - request: FastAPI Request object.
        - call_next: Callback function for the next middleware or endpoint.

        Returns:
        - response: FastAPI Response object.
        """

        colombia_timezone = pytz.timezone('America/Bogota')

        # Get the current time in UTC
        current_time_utc = datetime.utcnow()

        # Convert the current time to the Colombia timezone
        current_time_colombia = current_time_utc.astimezone(colombia_timezone)

        # Continue handling the request
        request.state.current_time_colombia = current_time_colombia

        response = await call_next(request)
        return response
