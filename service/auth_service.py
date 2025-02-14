import jwt
from os import getenv
from common.keys import EnvKey
from datetime import datetime

class AuthJwtPayload:
    customer_id: str
    wallet_id: str

    def __init__(self, customer_id: str, wallet_id: str):
        self.customer_id = customer_id
        self.wallet_id = wallet_id

class AuthService:
    algorithm: str = "HS256"
    def generate_jwt_token(self, customer_id: str, wallet_id: str) -> str:
        secret = getenv(EnvKey.JwtSecretKey.value)
        payload = {
            "customer_id": customer_id,
            "wallet_id": wallet_id,
            "exp": datetime.now()
        }
        return jwt.encode(payload, secret, self.algorithm)
    
    def parse_jwt_token_payload(self, token: str) -> AuthJwtPayload | None:
        secret = getenv(EnvKey.JwtSecretKey.value)
        
        try:
            decoded = jwt.decode(token, secret, self.algorithm, verify=True)
            customer_id = decoded["customer_id"]    
            wallet_id = decoded["wallet_id"]

            return AuthJwtPayload(customer_id, wallet_id)
        except Exception as e:
            return None
        

