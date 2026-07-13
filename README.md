# Kiro Birthday

A small Python utility that fetches google.com and logs the HTTP response status code.

## Installation

Requires the `requests` library:

```bash
pip install requests
```

## Usage

```python
from fetch_google import fetch_google_status

fetch_google_status()
```

This logs the HTTP status code (e.g. `200`) to stdout via Python's `logging` module. Connection errors, timeouts, and other request failures are caught and logged as errors.

## Files

- `fetch_google.py`: Contains `fetch_google_status()`, which sends a GET request to `https://www.google.com` with a 10-second timeout and logs the result.
