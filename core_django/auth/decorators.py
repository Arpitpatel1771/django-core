from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from core_django.constants import (
    UNAUTHORIZED_401_RESPONSE_DATA,
    FORBIDDEN_403_RESPONSE_DATA,
    TOKEN_NOT_FOUND_401_RESPONSE_DATA,
)
from core_django.auth.utils import (
    validate_token_against_secret,
    authorize_user_for_views,
)


def authorize(groups=[]):
    def decorator(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            auth_value: str = request.META.get("HTTP_AUTHORIZATION")

            # Check if a token exists in the request headers
            if type(auth_value) != str or auth_value.strip() == "":
                raise Response(
                    data=TOKEN_NOT_FOUND_401_RESPONSE_DATA,
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            else:
                auth_value = auth_value.strip()

            token = auth_value.split(" ")[-1]

            # Check if the token is valid by verifying it from UMS
            if not validate_token_against_secret(token):
                return Response(
                    data=UNAUTHORIZED_401_RESPONSE_DATA,
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # Check if the user is authorized to access the view
            if not authorize_user_for_views(token, groups):
                return Response(
                    data=FORBIDDEN_403_RESPONSE_DATA, status=status.HTTP_403_FORBIDDEN
                )

            return function(request, *args, **kwargs)

        return wrapper

    return decorator
