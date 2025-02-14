from models.wallet import Wallet
from models.transaction import *
from dataclasses import asdict, dataclass
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


@dataclass
class WalletDepositResponseData:
    def __init__(self, id: str, deposited_by: str, status: str, deposited_at: str, amount: int, reference_id: str):
        self.id = id
        self.deposited_by = deposited_by
        self.status = status
        self.deposited_at = deposited_at
        self.amount = amount
        self.reference_id = reference_id

    id: str
    deposited_by: str
    status: str
    deposited_at: str
    amount: int
    reference_id: str

@dataclass
class WalletDepositResponse:
    wallet: WalletDepositResponseData
    
    def __init__(self, data: WalletDepositResponseData):
        self.wallet = data
    
def convert_transaction_model_to_wallet_deposit_response(model: Transaction | None, customer_id: str) -> dict[str, any] | None:
    if model is None:
        return None
    
    resp_data = WalletDepositResponseData(str(model.id), customer_id, model.status, time.convert_timestamp_to_iso_format(model.created_at), model.amount, model.reference_id)
    return asdict(WalletDepositResponse(resp_data))

@dataclass
class WalletWithdrawResponseData:
    def __init__(self, id: str, withdrawn_by: str, status: str, withdrawn_at: str, amount: int, reference_id: str):
        self.id = id
        self.withdrawn_by = withdrawn_by
        self.status = status
        self.withdrawn_at = withdrawn_at
        self.amount = amount
        self.reference_id = reference_id

    id: str
    withdrawn_by: str
    status: str
    withdrawn_at: str
    amount: int
    reference_id: str

@dataclass
class WalletWithdrawResponse:
    wallet: WalletWithdrawResponseData
    
    def __init__(self, data: WalletWithdrawResponseData):
        self.wallet = data
    
def convert_transaction_model_to_wallet_withdraw_response(model: Transaction | None, customer_id: str) -> dict[str, any] | None:
    if model is None:
        return None
    
    resp_data = WalletWithdrawResponseData(str(model.id), customer_id, model.status, time.convert_timestamp_to_iso_format(model.created_at), model.amount, model.reference_id)
    return asdict(WalletWithdrawResponse(resp_data))