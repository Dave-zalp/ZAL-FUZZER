import json
import time
import requests
import os
import logging
import sys
from collections import defaultdict
import threading

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Define color codes for logging
RED = "\33[91m"
GREEN = "\033[32m"
YELLOW = "\033[93m"


class FuzzerEngine:

    def __init__(self, args):
        self.args = args
        self.res = self.get_args()

    def get_args(self):
        new_contents = dict()
        for name, value in vars(self.args).items():
            new_contents[name] = value
        return defaultdict(lambda: None, new_contents)  # Missing keys return None

    def make_request(self, url):
        req = self.get_args()
        try:
            body = requests.request(
                method='GET',
                url=url,
                headers=req['headers'],
                cookies=req['cookies']
            )
            code = body.status_code
            color = RED if 400 <= code <= 599 else (YELLOW if 300 <= code <= 399 else GREEN)
            return {
                'url': url,
                'statusCode': code
            }
        except ConnectionError:
            return f"{color}[404]"

    def get_statuscode(self):
        req = self.get_args()
        try:
            f = open(req['wordlistPath'], 'r')
            start = 1
            for x in f.readlines():
                logger.info(f'{YELLOW}{start}')
                start = start + 1
                status_code = self.make_request(x.strip())  # Preserve the color formatting
                logger.info(f'{GREEN}{x.strip()} {status_code}')
                print("")
                time.sleep(2)

        except FileNotFoundError:
            logger.error("Appended wordlist not Found !")




#Add multithreading to this




