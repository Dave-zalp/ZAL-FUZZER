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
RED = "\33[91m"
GREEN = "\033[32m"
YELLOW = "\033[93m"


class TestRequest:

    def __init__(self,url):
        self.url = url
        self.result = self.test_req()



    def test_req(self):
        option = 'yes'

        try:
            logger.info(f"{YELLOW}[+] Checking if the host is active")
            time.sleep(3)
            r = requests.request(method='GET', url=self.url, allow_redirects=True)

            if r.status_code not in {200, 400, 201, 204, 301, 302}:
                logger.warning([f"[-] Host returned a {r.status_code} status Code "])

                while True:
                    option = input("Do you wish to continue? [yes/no]: ").strip().lower()
                    if option in {"yes", "no"}:
                        break
                    logger.warning("Invalid input. Please enter 'yes' or 'no'.")
            else:
                logger.info(f"{GREEN}[+] Request was successful with a {r.status_code} Status Code  ")
            time.sleep(3)

        except requests.exceptions.ConnectionError:
            logger.error(f"{RED}[-] Connection Error/ Invalid Host")
            option = 'no'

        except requests.exceptions.RequestException:
            logger.error(f"{RED}[-] An Error Occurred")
            option = 'no'

        return option
