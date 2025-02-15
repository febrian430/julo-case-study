from repository.wallet_repository import WalletRepository
from common.exceptions import *
from models.wallet import *
from dto import dtos
from models.transaction import *


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
        return dtos.convert_model_to_enabled_wallet_response(wallet)

    def disable_wallet(self, wallet_id: str) -> dtos.DisableWalletResponse:
        wallet = self.repository.find_wallet_by_id(wallet_id, need_balance=True)
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.disabled_at is not None:
            raise WalletDisabledError
        
        wallet = self.repository.disable_wallet(wallet)
        return dtos.convert_model_to_disable_wallet_response(wallet)

    def deposit(self, wallet_id: str, customer_id: str, amount: int, reference_id: str) -> dtos.WalletDepositResponse:
        wallet = self.repository.find_wallet_by_id(wallet_id)
        
        transaction_type  = TransactionType.DEPOSIT
        status = TransactionStatus.SUCCESS
        
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.disabled_at is not None:
            status = TransactionStatus.FAILED
        
        transaction = self.repository.find_transaction_by_reference_id(reference_id)
        if transaction != None:
            raise DuplicateTransactionReferenceId
        
        transaction = self.repository.put_transaction(wallet_id, transaction_type, amount, status, reference_id)
        
        if wallet.disabled_at is not None:
            raise WalletDisabledError
        
        return dtos.convert_transaction_model_to_wallet_deposit_response(transaction, customer_id)
        
    def withdraw(self, wallet_id: str, customer_id: str, amount: int, reference_id: str) -> dtos.WalletDepositResponse:
        wallet = self.repository.find_wallet_by_id(wallet_id, need_balance=True)
        
        transaction_type  = TransactionType.WITHDRAW
        status = TransactionStatus.SUCCESS
        
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.disabled_at is not None or wallet.balance < amount:
            status = TransactionStatus.FAILED
        
        transaction = self.repository.find_transaction_by_reference_id(reference_id)
        if transaction != None:
            raise DuplicateTransactionReferenceId
        
        transaction = self.repository.put_transaction(wallet_id, transaction_type, amount, status, reference_id)
        
        if wallet.disabled_at is not None:
            raise WalletDisabledError
        
        return dtos.convert_transaction_model_to_wallet_deposit_response(transaction, customer_id)
        
    def get_wallet(self, wallet_id: str) -> dtos.EnabledWalletResponseData:
        wallet = self.repository.find_wallet_by_id(wallet_id, need_balance=True)
        if wallet is None:
            raise WalletNotFoundError
        elif wallet.disabled_at is not None:
            raise WalletDisabledError
        
        return dtos.convert_model_to_enabled_wallet_response(wallet)