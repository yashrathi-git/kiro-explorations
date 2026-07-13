"""
Module to fetch data from Google.

This module provides a function to make an HTTP GET request to google.com
and log the response status code. It relies on the `requests` library.
"""

import logging
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_google_status():
    """
    Fetches the homepage of google.com and logs the HTTP status code.

    This function sends an HTTP GET request to 'https://www.google.com'.
    If the request is successful, it logs the status code (e.g., 200).
    It should handle potential exceptions such as connection errors or
    timeouts and log appropriate error messages.

    Returns:
        None
    """
    try:
        response = requests.get("https://www.google.com", timeout=10)
        logger.info("HTTP status code: %d", response.status_code)
    except requests.exceptions.ConnectionError:
        logger.error("Failed to connect to google.com")
    except requests.exceptions.Timeout:
        logger.error("Request to google.com timed out")
    except requests.exceptions.RequestException as e:
        logger.error("An error occurred: %s", e)

