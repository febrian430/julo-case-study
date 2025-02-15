import pytz
from os import getenv
from common.keys import EnvKey
from datetime import datetime

def convert_timestamp_to_iso_format(time: datetime) -> str:
    tz = pytz.timezone(getenv(EnvKey.ServerTimezone.value, "Asia/Jakarta"))
    return datetime.fromtimestamp(time.timestamp(), tz).isoformat()