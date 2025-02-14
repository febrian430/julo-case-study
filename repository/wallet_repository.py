from models.wallet import Wallet
from uuid import uuid4
from datetime import datetime

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
        