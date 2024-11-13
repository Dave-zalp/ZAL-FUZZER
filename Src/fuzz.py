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


class FuzzerEngine:

    def __init__(self, args):
        self.args = args
        self.res = self.get_args()

    def get_args(self):
        new_contents = dict()
        for name, value in vars(self.args).items():
            new_contents[name] = value
        return new_contents

