from enum import Enum

class EnvKey(Enum):
    JwtSecretKey = "JWT_SECRET_KEY"
    ServerTimezone = "SERVER_TIMEZONE"


class HeaderKey(Enum):
    Authorization = "Authorization"