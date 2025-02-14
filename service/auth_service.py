import jwt
from os import getenv
from common.env_keys import EnvKey

class AuthService:
    def generate_jwt_token(self, customer_id: str, wallet_id: str) -> str:
        secret = getenv(EnvKey.JwtSecretKey.value)
        payload = {
            "customer_id": customer_id,
            "wallet_id": wallet_id,
        }
        return jwt.encode(payload, secret, "HS256")