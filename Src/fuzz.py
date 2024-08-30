import json
import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


class FuzzerEngine():

    def __init__(self):
        self.set_config()

    def set_config(self):
        file_path = os.path.join(os.path.dirname(__file__), '../config.json')
        try:
            with open(file_path, 'r') as file:
                new_file = json.load(file)
                for categories , indexes in new_file.items():
                    for keys,values in indexes.items():
                        setattr(self,keys,values)
        except FileNotFoundError:
            logger.error(f"{file_path} not Found")


