from models.wallet import Wallet
from uuid import uuid4
from datetime import datetime
from common.exceptions import WalletAlreadyEnabledError

class WalletRepository:
    def create_wallet(self, customer_id: str) -> str:
        wallet_id = str(uuid4())
        Wallet.create(
            id = wallet_id,
            customer_id = customer_id,
            enabled_at = None,
            disabled_at = datetime.now().timestamp(),
        )

        return wallet_id

    def find_wallet_by_id(self, wallet_id: str) -> Wallet:
        record = Wallet.get_by_id(wallet_id)
        return record

    def enable_wallet(self, wallet: Wallet) -> Wallet:
        now = datetime.now().timestamp()
        wallet.enabled_at = now
        wallet.disabled_at = None
        wallet.save()
        return wallet
    
    def disable_wallet(self, wallet: Wallet) -> Wallet:
        now = datetime.now().timestamp()
        wallet.disabled_at = now
        wallet.enabled_at = None
        wallet.save()
        return wallet