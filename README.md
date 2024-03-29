# discord-timestamps

**discord-timestamps** is a Python library designed to generate properly-formatted dynamic timestamps for Discord messages. It extends its functionality to support a wide range of input types including Python's `datetime.datetime`, `int` (Unix timestamp), `float` (Unix timestamp with fractions), and Arrow objects, enabling more flexible timestamp formatting within your Discord applications.

```python
from discord_timestamps import format_timestamp, TimestampType
from datetime import datetime
import arrow

# Example using datetime
print(format_timestamp(datetime(2021, 11, 20, 12, 0, 0)))
# Output: '<t:1637409600>'

# Example using Arrow and specifying a TimestampType
print(format_timestamp(arrow.now(), TimestampType.RELATIVE))
# Output: '<t:current_unix_time:R>'
```

[![Downloads](https://pepy.tech/badge/discord-timestamps)](https://pepy.tech/project/discord-timestamps)
[![Supported Versions](https://img.shields.io/pypi/pyversions/discord-timestamps.svg)](https://pypi.org/project/discord-timestamps)
[![Testing](https://img.shields.io/github/workflow/status/bsoyka/discord-timestamps/Test%20with%20pytest?label=tests)](https://github.com/bsoyka/discord-timestamps/actions?query=workflow%3A"Test+with+pytest")
[![License](https://img.shields.io/pypi/l/discord-timestamps)](https://github.com/bsoyka/discord-timestamps/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/discord-timestamps?label=latest)](https://pypi.org/project/discord-timestamps)

## Installation

You can easily install **discord-timestamps** via PyPI:

```console
$ pip install discord-timestamps
```

This library officially supports Python 3.6 and newer.

## Features

- **Flexible Timestamp Input**: Supports `datetime.datetime`, `int`, `float`, and Arrow object inputs.
- **Multiple Formatting Options**: Customize your timestamps with various formatting styles (e.g., Short Time, Long Time, Short Date, Long Date, Relative).
- **Easy Integration**: Designed to be straightforward and intuitive for integration into Discord bots and other applications.

## API Reference

For detailed documentation, including all available formatting options and usage examples, please visit the [wiki](https://github.com/bsoyka/discord-timestamps/wiki).
