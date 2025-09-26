import time
import random

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"

colors = [RED, BLUE, GREEN, YELLOW, PURPLE, CYAN, END]
options = random.choice(colors)




def print_banner():
     banner = f"""{options}
                
                ███████╗ █████╗ ██╗      ███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
                ╚══███╔╝██╔══██╗██║      ██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
                  ███╔╝ ███████║██║█████╗█████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
                 ███╔╝  ██╔══██║██║╚════╝██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
                ███████╗██║  ██║███████╗ ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
                ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                
                                  An Automatic Web Fuzzer.
                                  Zalparus Dev
                                  Made by https://t.me/moratadave
                                                                                          
                
                """
     print(banner)
     time.sleep(3)


