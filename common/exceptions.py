class WalletNotFoundError(Exception):
    def __init__(self):
        super().__init__("wallet not found")

class WalletAlreadyEnabledError(Exception):
    def __init__(self):
        super().__init__("wallet is already enabled")

class WalletAlreadyDisabledError(Exception):
    def __init__(self):
        super().__init__("wallet is already disabled")