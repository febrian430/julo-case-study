from fastapi import APIRouter, Form, status, Request, Depends
from routers.json_response_builder import *
from repository.wallet_repository import WalletRepository
from service.wallet_service import WalletService
from service.auth_service import AuthService
from logger import logger
from middleware.auth import parse_user_from_token
from common.exceptions import *
from routers.validations import validate_init_wallet

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
    
    try:
        validate_init_wallet(customer_xid)
        
        wallet_id = service.create_wallet(customer_xid)
        token = authService.generate_jwt_token(customer_xid, wallet_id)

        return success_response(
            status_code=status.HTTP_201_CREATED,
            content={"token": token}
        )
    except ValidationError as ve:
        return validation_error(ve)
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
    
@router.post("/wallet", dependencies=[Depends(parse_user_from_token)])
def enable_wallet(request: Request):
    try:
        wallet = service.enable_wallet(request.state.wallet_id)
       
        return success_response(
            status_code=status.HTTP_200_OK,
            content=wallet
        )
    except WalletEnabledError:
        return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="Already enabled"
        )
    except WalletNotFoundError:
         return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error="wallet not found"
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
        
    
@private_router.patch("/wallet", dependencies=[Depends(parse_user_from_token)])
def disable_wallet(request: Request):
    try:
        wallet = service.disable_wallet(request.state.wallet_id)
       
        return success_response(
            status_code=status.HTTP_200_OK,
            content= wallet
        )
    except WalletDisabledError:
        return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="Already disabled"
        )
    except WalletNotFoundError:
         return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error="wallet not found"
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
        
@private_router.post("/wallet/deposits", dependencies=[Depends(parse_user_from_token)])
def deposit(
        request: Request, 
        amount: int = Form(0),
        reference_id: str = Form("")
    ):
    
    # TODO: add validation
    
    try:
        resp = service.deposit(request.state.wallet_id, request.state.customer_id, amount, reference_id)
       
        return success_response(
            status_code=status.HTTP_200_OK,
            content=resp
        )
    except WalletDisabledError:
        return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="Wallet is disabled"
        )
    except WalletNotFoundError:
         return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error="wallet not found"
        )
    except DuplicateTransactionReferenceId:
         return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="reference id already exists"
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
        

@private_router.post("/wallet/withdrawals", dependencies=[Depends(parse_user_from_token)])
def withdraw(
        request: Request, 
        amount: int = Form(0),
        reference_id: str = Form("")
    ):
    
    # TODO: add validation
    
    try:
        resp = service.withdraw(request.state.wallet_id, request.state.customer_id, amount, reference_id)
       
        return success_response(
            status_code=status.HTTP_200_OK,
            content= resp
        )
    except WalletDisabledError:
        return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="Wallet is disabled"
        )
    except WalletNotFoundError:
         return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error="wallet not found"
        )
    except DuplicateTransactionReferenceId:
         return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="reference id already exists"
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
        
@private_router.get("/wallet", dependencies=[Depends(parse_user_from_token)])
def get_wallet(request: Request, ):
    
    try:
        resp = service.get_wallet(request.state.wallet_id)
       
        return success_response(
            status_code=status.HTTP_200_OK,
            content=resp
        )
    except WalletDisabledError:
        return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="Wallet is disabled"
        )
    except WalletNotFoundError:
         return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error="wallet not found"
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
        
        
@private_router.get("/wallet/transactions", dependencies=[Depends(parse_user_from_token)])
def get_wallet(request: Request, ):
    
    try:
        resp = service.get_wallet_transactions(request.state.wallet_id)
       
        return success_response(
            status_code=status.HTTP_200_OK,
            content=resp
        )
    except WalletDisabledError:
        return error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error="Wallet is disabled"
        )
    except WalletNotFoundError:
         return error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error="wallet not found"
        )
    except Exception as e:
        logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
        return internal_server_error_response(e)
        
