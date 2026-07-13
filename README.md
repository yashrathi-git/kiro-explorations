# Kiro Explorations

The primary purpose of this project is to demonstrate **Kiro's `update-docs` hook**, which automatically updates documentation as code changes are made within the repository.

By configuring a post-tool-use hook (`.kiro/hooks/update-docs.json`), any modifications, creations, or deletions of source files trigger a background agent that inspects the code changes and synchronizes the documentation/README in real-time.

## Demo Application

This project also includes a small Python utility as a demo application.

### Installation

Requires the `requests` library:

```bash
pip install requests
```

### Usage

```python
from demo.fetch_google import fetch_google_status

fetch_google_status()
```

This utility fetches `google.com` and logs the HTTP response status code (e.g. `200`) to stdout via Python's `logging` module. Connection errors, timeouts, and other request failures are caught and logged as errors.

### Project Structure

- `demo/fetch_google.py`: Contains `fetch_google_status()`, which sends a GET request to `https://www.google.com` with a 10-second timeout and logs the result.
- `.kiro/hooks/update-docs.json`: The Kiro hook definition that manages automatic documentation updates.
