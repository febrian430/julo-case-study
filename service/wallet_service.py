from repository.wallet_repository import WalletRepository
from common.exceptions import *
from models.wallet import *
from dto import dtos


class WalletService:
    repository: WalletRepository

    def __init__(self, repository: WalletRepository):
        self.repository = repository

    def create_wallet(self, customer_id: str) -> str:
        return self.repository.create_wallet(customer_id)
    
    def enable_wallet(self, wallet_id: str) -> dtos.EnableWalletResponse:
        wallet = self.repository.find_wallet_by_id(wallet_id)
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.enabled_at is not None:
            raise WalletEnabledError
        
        wallet = self.repository.enable_wallet(wallet)
        return dtos.convert_model_to_enable_wallet_response(wallet)

    def disable_wallet(self, wallet_id: str) -> dtos.DisableWalletResponse:
        wallet = self.repository.find_wallet_by_id(wallet_id)
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.disabled_at is not None:
            raise WalletDisabledError
        
        wallet = self.repository.disable_wallet(wallet)
        return dtos.convert_model_to_disable_wallet_response(wallet)

    def deposit(self, wallet_id: str, amount: int, reference_id: str):
        wallet = self.repository.find_wallet_by_id(wallet_id)
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.disabled_at is not None:
            raise WalletDisabledError