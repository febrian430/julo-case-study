from fastapi.responses import JSONResponse
from fastapi import status
from logger import logger
import traceback

def build_json_response(status_code: int, status: str, content: any) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "status": status,
            "data": content
        }
    )
    
def error_response(status_code: int, error_msg: str) -> JSONResponse:
    return build_json_response(status_code, "fail", {
        "error": error_msg
    })

def success_response(status_code: int, content: any) -> JSONResponse:
    return build_json_response(status_code, "success", content)

def internal_server_error_response(e: Exception) -> JSONResponse:
    logger.error(f'unexpected error: {e}\n{traceback.format_exc()}')
    return error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "unknown error")