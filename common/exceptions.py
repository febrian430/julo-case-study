class WalletNotFoundError(Exception):
    def __init__(self):
        super().__init__("wallet not found")

class WalletEnabledError(Exception):
    def __init__(self):
        super().__init__("wallet is already enabled")

class WalletDisabledError(Exception):
    def __init__(self):
        super().__init__("wallet is already disabled")