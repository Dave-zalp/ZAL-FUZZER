import json
import logging
import time

from Src import banner
import argparse
from Src import fuzz

# Set up argument parsing
parser = argparse.ArgumentParser(description='Enter Any of the following arguments to continue.')
parser.add_argument('-u', '--url', help='Enter the URL of target and use FUZZ on the path to fuzz')
parser.add_argument('-w', '--wordlistPath', help='Enter path to custom wordlist')
parser.add_argument('-c', '--cookies', help='Enter Custom cookies to use')
parser.add_argument('-hs', '--headers', help='Enter your Custom request header/headers separated by comma', required=False)
parser.add_argument('-mc', '--statusCode', help='Enter Request status to match', required=False)
parser.add_argument('-ms', '--ContentLength', help='Enter Content length to match', required=False)
parser.add_argument('-th', '--threads', help='Enter Number of Threads', required=False)
parser.add_argument('-pr', '--proxies', help='Enter Custom Proxies', required=False)

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

def main():
    # Filter out arguments that are not None
    set_args = {k: v for k, v in args_dict.items() if v is not None}

    # Print the banner and the arguments
    banner.print_banner()
    logger.info(f'{YELLOW}+----------------------------------------------------------------------------------------------+{END}')

    if set_args:
        for key, val in set_args.items():
            logger.info(f'--> {YELLOW}{key}                      :{GREEN}{val}{END}')

    logger.info(f'-->{YELLOW}Method                             :{GREEN}GET{END}')
    logger.info(f'{YELLOW}+----------------------------------------------------------------------------------------------+{END}\n')
    time.sleep(2)

    # Load the configuration file
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)

        # Update the JSON data with values from set_args
        updated = False
        for section, items in config_data.items():
            for item in set_args:
                # Check if the item is in the current section
                if item in items:
                    items[item] = set_args[item]
                    updated = True

        # Write the updated JSON data back to the file
        if updated:
            with open('config.json', 'w') as config_file:
                json.dump(config_data, config_file, indent=4)
            logger.info(f"{GREEN}Config file updated successfully.{END}")

            # Initialize the fuzzer engine
            fuzzer = fuzz.FuzzerEngine()

        else:
            logger.info(f"{YELLOW}No matching keys found in the config file.{END}")

    except FileNotFoundError:
        logger.error(f"{RED}Error: config.json file not found.{END}")
    except json.JSONDecodeError:
        logger.error(f"{RED}Error: Failed to decode JSON from config.json.{END}")

if __name__ == '__main__':
    main()
