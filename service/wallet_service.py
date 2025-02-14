from repository.wallet_repository import WalletRepository

class WalletService:
    repository: WalletRepository

    def __init__(self, repository: WalletRepository):
        self.repository = repository

    def create_wallet(self, customer_id: str) -> str:
        return self.repository.create_wallet(customer_id)

