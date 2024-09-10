import json
import logging
import time
import argparse
from Src import banner
from Src import fuzz

# Set up argument parsing
parser = argparse.ArgumentParser(description='Enter any of the following arguments to continue.')
parser.add_argument('-u', '--url', help='Enter the URL of target and use FUZZ on the path to fuzz')
parser.add_argument('-w', '--wordlistPath', help='Enter path to custom wordlist')
parser.add_argument('-c', '--cookies', help='Cookies in JSON format', default='{}', required=False)
parser.add_argument('-H', '--headers', help='Headers in format "Key: Value, Key2: Value2"', default='', required=False)
parser.add_argument('-mc', '--statusCode', help='Enter Request status to match', required=False)
parser.add_argument('-ms', '--ContentLength', help='Enter Content length to match', required=False)
parser.add_argument('-th', '--threads', help='Enter Number of Threads', required=False)
parser.add_argument('-pr', '--proxies', help='Proxies in JSON format', default='{}', required=False)

args = parser.parse_args()
args_dict = vars(args)

# Define color codes for logging
RED = "\33[91m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
END = "\033[0m"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def parse_headers(header_string):
    headers = {}
    header_string = header_string.strip().strip('"')
    header_entries = header_string.split(',')
    for entry in header_entries:
        if ':' in entry:
            key, value = entry.split(':', 1)
            key = key.strip()
            value = value.strip()
            headers[key] = value
    return headers

def update_config(config_data, set_args):
    # Update RequiredArguments
    if 'url' in set_args or 'wordlistPath' in set_args or 'Timeout' in set_args or 'threads' in set_args or 'method' in set_args:
        for key in ['url', 'wordlistPath', 'Timeout', 'threads', 'method']:
            if key in set_args:
                config_data['RequiredArguments'][key] = set_args[key]

    # Update HttpArguments
    if 'cookies' in set_args:
        config_data['HttpArguments']['cookies'] = set_args['cookies']
    if 'headers' in set_args:
        config_data['HttpArguments']['headers'] = set_args['headers']
    if 'proxies' in set_args:
        config_data['HttpArguments']['proxies'] = set_args['proxies']
    if 'FollowRedirects' in set_args:
        config_data['HttpArguments']['FollowRedirects'] = set_args['FollowRedirects']

    # Update MatchArguments
    if 'statusCode' in set_args:
        config_data['MatchArguments']['statusCode'] = set_args['statusCode']
    if 'ContentLength' in set_args:
        config_data['MatchArguments']['ContentLength'] = set_args['ContentLength']

def main():
    # Filter out arguments that are not None or empty
    set_args = {k: v for k, v in args_dict.items() if v not in (None, '{}', {}, [], '', ())}

    # Convert JSON strings to dictionaries where applicable
    for key in ['cookies', 'headers', 'proxies']:
        if key in set_args:
            if key == 'headers':
                set_args[key] = parse_headers(set_args[key])
            else:
                try:
                    set_args[key] = json.loads(set_args[key])
                except json.JSONDecodeError:
                    logger.error(f"{RED}Error parsing {key}. Ensure it's valid JSON.{END}")
                    set_args[key] = {}

    # Print the banner and the arguments
    banner.print_banner()
    logger.info(f'{YELLOW}+----------------------------------------------------------------------------------------------+{END}')

    # Print all Arguments
    if set_args:
        for key, val in set_args.items():
            logger.info(f'--> {YELLOW}{key}                      :{GREEN}{val}{END}')

    logger.info(f'-->{YELLOW}Method                             :{GREEN}GET{END}')
    logger.info(f'{YELLOW}+----------------------------------------------------------------------------------------------+{END}\n')
    time.sleep(2)

    # Load and update the configuration file
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)

        update_config(config_data, set_args)

        # Write the updated JSON data back to the file
        with open('config.json', 'w') as config_file:
            json.dump(config_data, config_file, indent=4)
        logger.info(f"{GREEN}Config file updated successfully.{END}")

        # Initialize the fuzzer engine
        fuzzer = fuzz.FuzzerEngine()

    except FileNotFoundError:
        logger.error(f"{RED}Error: config.json file not found.{END}")
    except json.JSONDecodeError:
        logger.error(f"{RED}Error: Failed to decode JSON from config.json.{END}")

if __name__ == '__main__':
    main()

