from service.auth_service import AuthService
from fastapi import Request, status, HTTPException
from common.keys import HeaderKey
from logger import logger

auth_service = AuthService()

def parse_user_from_token(request: Request):
    value = request.headers.get(HeaderKey.Authorization.value)
    if value is None:
        logger.info("no token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "status": "fail"
            }
        )
    
    split_values = value.split(" ", maxsplit=1)
    if len(split_values) < 2:
        logger.info("invalid format")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "status": "fail"
            }
        )
    key = split_values[0]
    token = split_values[1]
    payload = auth_service.parse_jwt_token_payload(token)
    if key != "Token" or payload == None:
        logger.info("unable to parse jwt token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "status": "fail"
            }
        )

    request.state.wallet_id = payload.wallet_id
    request.state.customer_id = payload.customer_id