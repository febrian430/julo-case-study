from typing import Annotated
from fastapi import APIRouter, Form, status, Request, Depends
from fastapi.responses import JSONResponse
from repository.wallet_repository import WalletRepository
from service.wallet_service import WalletService
from service.auth_service import AuthService
from logger import logger
from middleware.auth import parse_user_from_token
from common.exceptions import *

router = APIRouter(
    prefix="/api/v1"
)

private_router = APIRouter(
    prefix="/api/v1"
)


repo = WalletRepository()
service = WalletService(repo)
authService = AuthService()

@router.post("/init")
def init_wallet(customer_xid: str|None = Form("")):
    if len(customer_xid) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content={
                "status": "fail", 
                "data": {
                    "customer_xid": ["Missing data for required field."]
                }
            }
        )
    try:
        wallet_id = service.create_wallet(customer_xid)
        token = authService.generate_jwt_token(customer_xid, wallet_id)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"status": "success", "data": {"token": token}}
        )
    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={"status":"fail"}
        )

@private_router.post("/wallet", dependencies=[Depends(parse_user_from_token)])
def enable_wallet(request: Request):
    try:
        wallet = service.enable_wallet(request.state.wallet_id)
       
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": "success",
                "data": wallet
            }
        )
    except WalletAlreadyEnabledError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "fail",
                "data": {
                    "error": "Already enabled"
                }
            }
        )
    except WalletNotFoundError:
         return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": "fail",
                "data": {
                    "error": "wallet not found"
                }
            }
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}')
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "fail",
                "data": {
                    "error": "unknown error"
                }
            }
        )
        
    
@private_router.patch("/wallet", dependencies=[Depends(parse_user_from_token)])
def disable_wallet(request: Request):
    try:
        wallet = service.disable_wallet(request.state.wallet_id)
       
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": "success",
                "data": wallet
            }
        )
    except WalletAlreadyDisabledError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "fail",
                "data": {
                    "error": "Already disabled"
                }
            }
        )
    except WalletNotFoundError:
         return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "status": "fail",
                "data": {
                    "error": "wallet not found"
                }
            }
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}')
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "fail",
                "data": {
                    "error": "unknown error"
                }
            }
        )
        
    
    