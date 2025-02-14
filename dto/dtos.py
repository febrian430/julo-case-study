from models.wallet import Wallet
from dataclasses import asdict, dataclass
import json
from common import time

@dataclass
class EnableWalletResponseData:
    def __init__(self, id: str, owned_by: str, status: str, enabled_at: str, balance: int):
        self.id = id
        self.owned_by = owned_by
        self.status = status
        self.enabled_at = enabled_at
        self.balance = balance

    id: str
    owned_by: str
    status: str
    enabled_at: str
    balance: int

@dataclass
class EnableWalletResponse:
    wallet: EnableWalletResponseData
    
    def __init__(self, data: EnableWalletResponseData):
        self.wallet = data
    
def convert_model_to_enable_wallet_response(model: Wallet | None) -> dict[str, any] | None:
    if model is None:
        return None
    
    wallet_data = EnableWalletResponseData(model.id, model.customer_id, "enabled" if model.enabled_at is not None else "disabled", time.convert_timestamp_to_iso_format(model.enabled_at), model.balance)
    return asdict(EnableWalletResponse(wallet_data))


@dataclass
class DisableWalletResponseData:
    def __init__(self, id: str, owned_by: str, status: str, disabled_at: str, balance: int):
        self.id = id
        self.owned_by = owned_by
        self.status = status
        self.disabled_at = disabled_at
        self.balance = balance

    id: str
    owned_by: str
    status: str
    disabled_at: str
    balance: int

@dataclass
class DisableWalletResponse:
    wallet: DisableWalletResponseData
    
    def __init__(self, data: DisableWalletResponseData):
        self.wallet = data
    
def convert_model_to_disable_wallet_response(model: Wallet | None) -> dict[str, any] | None:
    if model is None:
        return None
    
    wallet_data = DisableWalletResponseData(model.id, model.customer_id, "enabled" if model.enabled_at is not None else "disabled", time.convert_timestamp_to_iso_format(model.disabled_at), model.balance)
    return asdict(DisableWalletResponse(wallet_data))