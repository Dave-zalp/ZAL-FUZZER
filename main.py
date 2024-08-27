from Src import banner
import argparse

parser = argparse.ArgumentParser(description='Enter Any of the following arguments to continue.')
parser.add_argument('-u', '--url', help='Enter the URL of target')
parser.add_argument('-w', '--wordlist', help='Enter path to custom wordlist')
parser.add_argument('-c', '--cookies', help='Enter Custom cookies to use')
parser.add_argument('-hs', '--headers', help='Enter your Custom request header/headers seperated by comma',required=False)
parser.add_argument('-mc', '--status code', help='Enter Reqeust status to display',required=False)
parser.add_argument('-pr', '--proxies', help='Enter Custom Proxies',required=False)

args = parser.parse_args()

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"

if __name__ == '__main__':
    banner.print_banner()
    print(
        f'{YELLOW}+----------------------------------------------------------------------------------------------+\n'
        f'{YELLOW}URL                             :{args.url}\n'
        f'{BLUE}Wordlist                          :{args.wordlist}\n'
        f'{GREEN}Method                           :GET')
