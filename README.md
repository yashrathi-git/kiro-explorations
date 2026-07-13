# Kiro Explorations

The primary purpose of this project is to demonstrate **Kiro's `update-docs` hook**, which automatically updates documentation as code changes are made within the repository.

By configuring a post-tool-use hook (`.kiro/hooks/update-docs.json`), any modifications, creations, or deletions of source files trigger a background agent that inspects the code changes and synchronizes the documentation/README in real-time.

## Demo Video

🎥 Watch the workflow and integration in action: **[Kiro Demo Video (YouTube)](https://www.youtube.com/watch?v=9R1jKaEn1D8)**

## How Kiro Was Used

This repository was developed as a practical sandbox to learn, configure, and thoroughly test Kiro's event-driven agent hooks. Our workflow began by studying how Kiro executes hooks based on development events, focusing on how background agent tasks can automate tedious repo tasks. Next, we designed a custom `PostToolUse` hook (`.kiro/hooks/update-docs.json`) that listens for file-system changes. To test this in practice, we built a Python-based demo application that retrieves google.com and logs its HTTP response. We then structured the project properly, moving our script into a dedicated `demo/` folder, and modified the codebase to trigger our custom hook. Experimenting with different matchers, triggers, and agent prompts allowed us to refine the automation until it consistently updated our README as code evolved. We ultimately validated the pipeline by running and committing the changes, resulting in a fully functional, self-documenting system.

## Demo Application

This project includes a small Python utility as a demo application.

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
