from common.exceptions import ValidationError
from collections import defaultdict

def validate_init_wallet(customer_xid: str):
    errors_by_field: dict[str: list[str]] = defaultdict(list)
    
    if len(customer_xid) == 0:
        errors_by_field["customer_xid"].append("Missing data for required field.")
    
    if len(errors_by_field) > 0:
        raise ValidationError(errors_by_field)
    return

def validate_transaction_request(amount: int, reference_id: str):
    errors_by_field: dict[str: list[str]] = defaultdict(list)
    
    amount_field = "amount"
    ref_id_field = "reference_id"
    
    if amount <= 0:
        errors_by_field[amount_field].append("Must be greater than 0")
    
    if len(reference_id) == 0:
        errors_by_field[ref_id_field].append("Missing data for required fields")
    
    if len(errors_by_field) > 0:
        raise ValidationError(errors_by_field)
    return
    