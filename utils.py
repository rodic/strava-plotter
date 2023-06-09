import datetime


def date_to_days_since_epoch(date: datetime.date) -> int:
    """
    Converts a datetime.date object to the number of days since the epoch.
    """
    return (date - datetime.datetime.utcfromtimestamp(0).date()).days

def from_iso_date(date: str) -> datetime.date:
    """
    Convert date string in ISO format to datetime.date object.
    """
    return datetime.datetime.fromisoformat(date).date()

def date_to_timestamp(date: datetime.date) -> float:
    """
    Converts a datetime.date object to a timestamp.
    """
    return datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day
    ).timestamp()
