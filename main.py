import json
import os
import logging
import sys
import time
from Src import banner
from Src import test, fuzz
import argparse

# Define color codes for logging
RED = "\33[91m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
END = "\033[0m"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def main():
    # Print the banner and the arguments
    banner.print_banner()
    logger.info(
        f'{YELLOW}+----------------------------------------------------------------------------------------------+{END}')

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="ZALPARUS Web Fuzzer Configuration")
    parser.add_argument('-u', '--url', help='Enter the URL of target and use FUZZ on the path to fuzz', dest='url')
    parser.add_argument('-w', '--wordlistPath', help='File to Custom wordlist', dest='wordlistPath')
    parser.add_argument('-mc', '--matchCode', default="GET", help='Enter Request status to match', dest='statusCode',
                        required=False)
    parser.add_argument('-th', '--threads', default=10, help='Enter Number of Threads', type=int, dest='threads',
                        required=False)
    parser.add_argument('-H', '--headers', help='Enter Request Headers', dest='headers',
                        required=False)
    parser.add_argument('-C', '--cookies', help='Enter Request Cookies', dest='Cookies',
                        required=False)

    # Parse arguments
    args = parser.parse_args()

    url = args.url
    wordlist = args.wordlistPath
    statuscode = args.statusCode
    threads = args.threads

    # Print all Arguments
    for key, val in vars(args).items():
        logger.info(f'--> {YELLOW}{key}                      :{GREEN}{val}{END}')
    logger.info(
        f'{YELLOW}+----------------------------------------------------------------------------------------------+{END}\n')
    time.sleep(2)

    # Initialize a test request
    tester = test.TestRequest(url)

    if tester.result == 'no':
        logger.error(f"{RED} Exiting the script")
        time.sleep(2)
        sys.exit()

    # Locate the path to the wordlist and load the wordlist to the file
    try:
        # Read all lines from the wordlist
        with open(wordlist, 'r') as paths:
            lines = paths.readlines()

        # Process each line and prepare new content
        new_content = []
        for line in lines:
            line = line.strip()  # Remove any extra whitespace or newline
            newline = f"{url}/{line}\n"
            new_content.append(newline)

        # Write the modified lines back to the file
        with open(wordlist, 'w') as new_list:
            new_list.writelines(new_content)
        logger.info(f"{GREEN} Wordlist Updated !")

    except FileNotFoundError:
        logger.error(f"{RED}{wordlist} FILE NOT FOUND !")


    # Initialize Fuzzer Engine
    fuzzer = fuzz.FuzzerEngine(args)
    # print(fuzzer.get_args())
    print(fuzzer.main())


if __name__ == '__main__':
    main()
