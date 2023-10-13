TOKEN_NOT_FOUND_401_RESPONSE_DATA = {
    "status": "ERROR",
    "error": "A valid token is required in the request headers to access this view"
}

UNAUTHORIZED_401_RESPONSE_DATA = {
    "status": "ERROR",
    "error": "Token either has invalid credentials or is generated from an invalid source"
}

FORBIDDEN_403_RESPONSE_DATA = {
    "status": "ERROR",
    "error": "User is not allowed to access the view"
}

