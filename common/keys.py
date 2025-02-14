from enum import Enum

class EnvKey(Enum):
    JwtSecretKey = "JWT_SECRET_KEY"


class HeaderKey(Enum):
    Authorization = "Authorization"