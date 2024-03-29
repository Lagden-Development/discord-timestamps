"""Generation of properly-formatted dynamic timestamps for Discord messages"""

from typing import Union
import datetime
from arrow import Arrow

from .formats import TimestampType

__version__ = "1.0.2"

def format_timestamp(
    timestamp: Union[int, float, Arrow, datetime.datetime],
    timestamp_type: TimestampType = TimestampType.SHORT_DATETIME,
) -> str:
    """Generate a properly-formatted timestamp for Discord messages.

    This function supports int, float, Arrow, and datetime.datetime types for timestamps,
    automatically converting them to a Discord-friendly string format.

    Args:
        timestamp: The timestamp to format, can be an int (Unix timestamp), float (Unix timestamp with fractions),
                   Arrow object, or datetime.datetime instance.
        timestamp_type (TimestampType): The type of timestamp to format, determines the visual presentation in Discord.

    Returns:
        str: The formatted timestamp, ready to be included in Discord messages.
    """

    if isinstance(timestamp, (int, float)):
        # The timestamp is an int or float, convert it to an int
        int_timestamp = int(timestamp)

    elif isinstance(timestamp, Arrow):
        # The timestamp is an Arrow object, convert it to an int in UTC
        int_timestamp = timestamp.to('UTC').int_timestamp

    elif isinstance(timestamp, datetime.datetime):
        # The timestamp is a datetime object, convert it to UTC if not already, then to int
        if timestamp.tzinfo is not None:
            # Convert to UTC timezone if it has a timezone
            timestamp = timestamp.astimezone(datetime.timezone.utc)
        int_timestamp = int(timestamp.timestamp())

    # Combine the timestamp and the format
    return f"<t:{int_timestamp}:{timestamp_type.value}>"
