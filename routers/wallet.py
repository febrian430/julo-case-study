from typing import Annotated
from fastapi import APIRouter, Form, status
from fastapi.responses import JSONResponse
from repository.wallet_repository import WalletRepository
from service.wallet_service import WalletService
from logger import logger

router = APIRouter(
    prefix="/api/v1"
)

repo = WalletRepository()
service = WalletService(repo)

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
        service.create_wallet(customer_xid)
        return {"status": "success"}
    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={"status":"fail"}
        )
    
    