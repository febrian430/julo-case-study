from models.wallet import Wallet
from dataclasses import asdict, dataclass
import json
from common import time

class Response:
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)


@dataclass
class EnableWalletResponseData(Response):
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
class EnableWalletResponse(Response):
    wallet: EnableWalletResponseData
    
    def __init__(self, data: EnableWalletResponseData):
        self.wallet = data
    


def convert_model_to_enable_wallet_response(model: Wallet | None) -> dict[str, any] | None:
    if model is None:
        return None
    
    wallet_data = EnableWalletResponseData(model.id, model.customer_id, "enabled" if model.enabled_at is not None else "disabled", time.convert_timestamp_to_iso_format(model.enabled_at), model.balance)
    return asdict(EnableWalletResponse(wallet_data))