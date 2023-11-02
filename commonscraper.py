import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import time
from datetime import datetime

# Text styling
class textstylez:
    reset="\x1B[0m"
    dim="\x1B[2m"
    blink="\x1B[5m"
    negative="\x1B[7m"
    bigunderline="\x1B[21m"
    overline="\x1B[53m"
    bold="\x1B[1m"
    italic="\x1B[3m"
    underline="\x1B[4m"
    strike="\x1B[9m"
    fg_black="\x1B[30m"
    fg_red="\x1B[31m"
    fg_green="\x1B[32m"
    fg_yellow="\x1B[33m"
    fg_blue="\x1B[34m"
    fg_magenta="\x1B[35m"
    fg_cyan="\x1B[36m"
    fg_white="\x1B[37m"
    fg_stblack="\x1B[90m"
    fg_stred="\x1B[91m"
    fg_stgreen="\x1B[92m"
    fg_styellow="\x1B[93m"
    fg_stblue="\x1B[94m"
    fg_stmagenta="\x1B[95m"
    fg_stcyan="\x1B[96m"
    fg_stwhite="\x1B[97m"
    bg_black="\x1B[40m"
    bg_red="\x1B[41m"
    bg_green="\x1B[42m"
    bg_yellow="\x1B[43m"
    bg_blue="\x1B[44m"
    bg_magenta="\x1B[45m"
    bg_cyan="\x1B[46m"
    bg_white="\x1B[47m"
    bg_stblack="\x1B[100m"
    bg_stred="\x1B[101m"
    bg_stgreen="\x1B[102m"
    bg_styellow="\x1B[103m"
    bg_stblue="\x1B[104m"
    bg_stmagenta="\x1B[105m"
    bg_stcyan="\x1B[106m"
    bg_stwhite="\x1B[107m"

# Format Time
def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.2f}mins"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.2f}hrs"
    else:
        days = seconds / 86400
        return f"{days:.2f}days"

# Argument parser
class ArgumentParser:
    def __init__(self):
        self.args = {}
        self.parse_args()

    def parse_args(self):
        import sys
        args = sys.argv[1:]
        i = 0
        while i < len(args):
            arg = args[i]
            if arg.startswith('--'):
                key = arg[2:]
                value = True
                if i + 1 < len(args) and not args[i + 1].startswith('--'):
                    value = args[i + 1]
                    if ',' in value:
                        value = value.split(',')
                        value = [re.sub(r"['\"]", "", val) for val in value]
                    i += 1
                self.args[key] = value
            i += 1

    def get(self, key, default=None):
        return self.args.get(key, default)

argparser = ArgumentParser()

# Parse Arguments
proxies = None
if argparser.get('proxies'):

    proxies_list = argparser.get('proxies')
    if isinstance(proxies_list, str):
        proxies_list = [proxies_list]

    proxies = {}
    for proxy in proxies_list:
        proxy = re.sub("[$@&']","",proxy)
        proxy_parts = proxy.split(':')
        proxy_type = proxy_parts[0]
        proxy_address = ':'.join(proxy_parts[1:])
        proxy = re.sub(r'^https?://', '', proxy)
        proxies[proxy_type] = proxy
        if proxy_type == 'http':
            proxies['https'] = proxy

print(f"{textstylez.fg_cyan}Common Scraper - Common Words Scraper 1.0.0")
print(f"Copyright (c) 2023 gamemaster123356, All rights reserved.{textstylez.reset}")
print("")

print(f"{textstylez.fg_stred}{textstylez.blink}[!] Legal Disclaimer: Common Scraper is intended for legitimate and ethical web scraping purposes only.")
print(f"Using Common Scraper to scrape content from websites without proper authorization may violate the terms of service of those websites. Users are advised to obtain explicit permission from website owners before scraping their content. The developers assume no responsibility for any misuse or legal consequences resulting from the use of Common Scraper. Use this tool responsibly and in accordance with applicable laws and regulations.{textstylez.reset}")
print("")

if proxies:
    print(f"[*] Using proxies. Please beware that proxies may slow down scraping speeds.")
    print("")

# Get user input for URL
print(f"{textstylez.fg_yellow}{textstylez.bold}Enter the URL to scrape from or type exit() to exit.")
print(f"The URL MUST start with the scheme (http:// or https://){textstylez.reset}")
url_prompt = ''
while url_prompt == '':
    url_prompt = input(f">> ")

# Check if the prompt is exit() and then break the loop
if url_prompt == 'exit()':
    exit()

# Check if the prompt has a URL scheme (http:// or https://)
if not re.match(r'^https?://', url_prompt):
    print("")
    print(f"{textstylez.fg_stred}Error: Please include the URL scheme (http:// or https://){textstylez.reset}")
    print("")
    exit()
else:
    url = url_prompt



# Get user input for allowing redirects
print("")
print(f"{textstylez.fg_yellow}{textstylez.bold}Allow redirects? (Y/n) {textstylez.reset}")
redirect_prompt = input(f">> ")

if redirect_prompt == 'exit()':
    exit()

if redirect_prompt.lower() in ["n", "no"]:
    allow_redirects = False
else:
    allow_redirects = True



# Get user-defined elements
default_elements = ['p', 'a', 'li', 'h1', 'h2', 'h3']

print("")
print(f"{textstylez.fg_yellow}{textstylez.bold}Enter the elements to scrape (comma-separated), or press enter to use default setting:{textstylez.reset}")
user_elements = input(">> ")

if user_elements == 'exit()':
    exit()

elements = default_elements if user_elements.strip() == '' else [element.strip() for element in user_elements.split(',')]



# Get user-defined words to exclude
print("")
print(f"{textstylez.fg_yellow}{textstylez.bold}Enter words to exclude (comma-separated), or press enter to use default setting:{textstylez.reset}")
user_exclude_words = input(">> ")
print("")

if user_exclude_words == 'exit()':
    exit()

exclude_words = set(['a', 'an', 'the', 'is', 'are', 'and', 'or', 'in', 'on', 'at', 'you', 'may']) if user_exclude_words.strip() == '' else set([word.strip().lower() for word in user_exclude_words.split(',')])



# Start Scraping
current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(f"{textstylez.fg_styellow}[*] [{textstylez.fg_stblue}{current_datetime}{textstylez.fg_styellow}] Scraping Common Words...{textstylez.reset}")

elapsed_time = time.time()
try:
    r = requests.get(url, allow_redirects=allow_redirects, proxies=proxies)
    r.raise_for_status()  # Check for any HTTP errors
except requests.exceptions.RequestException as e:
    print(f"{textstylez.fg_stred}Error: Unable to retrieve content from {url}: {e}{textstylez.reset}")
    exit()

html_content = r.content

# Create a Beautiful Soup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements to scrape
word_list = []
for element in elements:
    elements_found = soup.find_all(element)
    for elem in elements_found:
        text = elem.get_text().strip()
        words = re.findall(r'\b\w+\b', text)
        word_list.extend(words)

# Filter out excluded words
filtered_words = [word.lower() for word in word_list if word.lower() not in exclude_words]

# Count the occurrences of each word
word_counts = Counter(filtered_words)

elapsed_time_format = format_time(time.time() - elapsed_time)
print(f"Done in {elapsed_time_format}")
print("")

# Save words to a file and print the most common words
if word_counts:
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"{textstylez.fg_styellow}[*] [{textstylez.fg_stblue}{current_datetime}{textstylez.fg_styellow}] Scraped Common Words:{textstylez.reset}")
    current_datetime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    file_name = f"scraped_words_{current_datetime}.txt"
    with open(file_name, "w") as f:
        for word, count in word_counts.most_common():
            f.write(f"{word}: {count}\n")
            print(f"{word}: {count}")
    print("")

    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"{textstylez.fg_styellow}[*] [{textstylez.fg_stblue}{current_datetime}{textstylez.fg_styellow}] Scraped words saved to '{file_name}'{textstylez.reset}")
else:
    print(f"{textstylez.fg_stred}No keywords found.{textstylez.reset}")
