from common.exceptions import ValidationError
from typing import List

def validate_init_wallet(customer_xid: str):
    errors_by_field: dict[str: List[str]] = {}
    
    errors_by_field["customer_xid"] = []
    if len(customer_xid) == 0:
        errors_by_field["customer_xid"].append("Missing data for required field.")
    
    if len(errors_by_field) > 0:
        raise ValidationError(errors_by_field)
    return