from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser,
    AuthCredentials
)

import base64
import binascii

# you can also encrypt these, or read them from an env var or from a database
ADMIN_USER = "Kiran"
ADMIN_PASS = "Password"


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        if(username, password) != (ADMIN_USER, ADMIN_PASS):
            return
        return AuthCredentials(["authenticated"]), SimpleUser(username)
