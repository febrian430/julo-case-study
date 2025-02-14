import pytz
from os import getenv
from common.keys import EnvKey
from datetime import datetime

def convert_timestamp_to_iso_format(timestamp: int) -> str:
    
    tz = pytz.timezone(getenv(EnvKey.ServerTimezone.value, "Asia/Jakarta"))
    return datetime.fromtimestamp(timestamp, tz).isoformat()