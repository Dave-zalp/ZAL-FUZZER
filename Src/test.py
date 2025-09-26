import json
import time
import requests
import os
import logging
import sys


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


# Define color codes for logging
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
END = "\033[0m"


class TestRequest:
    def __init__(self, url: str):
        self.url = url
        self.result = None

    def _prompt_continue(self) -> str:
        # Prompt user for continuation (yes/no).
        while True:
            option = input("Do you wish to continue? [yes/no]: ").strip().lower()
            if option in {"yes", "no"}:
                return option
            logger.warning("Invalid input. Please enter 'yes' or 'no'.")

    def test_req(self) -> str:
        """Check if the host is active and return 'yes' or 'no'."""
        allowed_statuses = {200, 201, 204, 301, 302, 400}

        try:
            logger.info(f"{YELLOW}[+] Checking if the host is active...{END}")
            time.sleep(1)

            # Faster check using HEAD
            try:
                r = requests.head(self.url, allow_redirects=True, timeout=5)
            except requests.RequestException:
                r = requests.get(self.url, allow_redirects=True, timeout=5)

            if r.status_code in allowed_statuses:
                logger.info(f"{GREEN}[+] Host is active with status {r.status_code}{END}")
                logger.info(f"{RED}[+] Logging out Test Response Info {END}")
                time.sleep(4)
                for key, value in r.headers.items():
                    logger.info(f"{GREEN}[+] {YELLOW}{key} :  {value}{END}")
                option = self._prompt_continue()
            else:
                logger.warning(f"{RED}[-] Host returned status {r.status_code}{END}")
                option = self._prompt_continue()

        except requests.exceptions.ConnectionError:
            logger.error(f"{RED}[-] Connection Error / Invalid Host{END}")
            option = "no"

        except requests.exceptions.RequestException as e:
            logger.error(f"{RED}[-] Request failed: {e}{END}")
            option = "no"

        self.result = option
        return option
