import json
import time
import requests
import os
import logging
import sys
from collections import defaultdict
import threading
from queue import Queue

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

    def make_request(self, queue):
        req = self.get_args()
        while not queue.empty():
            url = queue.get()
            try:
                body = requests.request(
                    method='GET',
                    url=url,
                    headers=req['headers'],
                    cookies=req['cookies'],
                )
                code = body.status_code
                color = RED if 400 <= code <= 599 else (YELLOW if 300 <= code <= 399 else GREEN)
                print(f"{color}URL: {url} | Status Code: {code}")
                # return {
                #     'url': url,
                #     'statusCode': code
                # }
            except ConnectionError:
                return f"{RED}[404]"
            finally:
                queue.task_done()

    # Read URLs from file
    def read_urls_from_file(self, filepath):

        try:
            with open(filepath, 'r') as file:
                urls = [line.strip() for line in file if line.strip()]
            return urls
        except FileNotFoundError:
            logger.error("Appended wordlist not Found !")

    def main(self):
        req = self.get_args()
        threads = req['threads']
        url_queue = Queue()
        urls = self.read_urls_from_file(req['wordlistPath'])

        # Add URLs to the queue
        for url in urls:
            url_queue.put(url)

        # Start threads
        thread_list = []
        for _ in range(threads):
            thread = threading.Thread(target=self.make_request, args=(url_queue,))
            thread.start()
            thread_list.append(thread)

        # Wait for all threads to complete
        for thread in thread_list:
            thread.join()






#Add request.sessions to enhance optimization
#Add another function in the script that would be manipulating the output of the result based on argument conditions from the user.




