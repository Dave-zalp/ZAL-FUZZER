import json
import time
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


class FuzzerEngine():

    def __init__(self):
        self.set_config()
        self.test_req()

    def parse_json_value(self, value):
        """Parses a value as JSON if possible, otherwise returns the value unchanged."""
        if isinstance(value, str):
            try:
                # Attempt to parse the value as JSON
                parsed_value = json.loads(value)
                # Ensure the parsed value is a dictionary for headers and proxies
                if isinstance(parsed_value, dict):
                    return parsed_value
            except json.JSONDecodeError:
                logger.warning(f"Warning: Failed to parse JSON from value: {value}")
        return value

    def set_config(self):
        file_path = os.path.join(os.path.dirname(__file__), '../config.json')
        try:
            with open(file_path, 'r') as file:
                new_file = json.load(file)
                for categories , indexes in new_file.items():
                    for keys,values in indexes.items():
                        # Parse specific keys that are expected to be dictionaries
                        if keys in ['headers', 'cookies', 'proxies']:
                            values = self.parse_json_value(values)
                        setattr(self,keys,values)
        except FileNotFoundError:
            logger.error(f"{file_path} not Found")

    def test_req(self):
        try:
            logger.info("[+] Initializing a sample test request")
            time.sleep(3)
            r = requests.request(method=self.method, url="https://google.com", headers=self.headers, cookies=self.cookies,proxies=self.proxies,timeout=self.Timeout)
            if r.status_code not in {200, 201, 204}:
                logger.warning(["<> Request headers might not be set successfully"])
            else:
                logger.info("[+] Request headers set successfully ")
        except requests.exceptions.RequestException:
            logger.error("[-] There was an issue with your request options. check the documentation and try again")
