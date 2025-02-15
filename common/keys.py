from enum import Enum

class EnvKey(Enum):
    JwtSecretKey = "JWT_SECRET_KEY"
    JwtExpiryInMinutes = "JWT_EXPIRY_IN_MINS"
    ServerTimezone = "SERVER_TIMEZONE"


class HeaderKey(Enum):
    Authorization = "Authorization"