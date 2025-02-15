from typing import List

class WalletNotFoundError(Exception):
    def __init__(self):
        super().__init__("wallet not found")

class WalletEnabledError(Exception):
    def __init__(self):
        super().__init__("wallet is already enabled")

class WalletDisabledError(Exception):
    def __init__(self):
        super().__init__("wallet is already disabled")
        
class DuplicateTransactionReferenceId(Exception):
    def __init__(self):
        super().__init__("transaction with reference id already exists")
        
class ValidationError(Exception):
    errors: dict[str: List[str]]
    
    def __init__(self, error_by_fields: dict[str: List[str]]):
        super().__init__("request validation error")
        self.errors = error_by_fields