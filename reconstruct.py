import os
import re
import subprocess

import requests

from interesting_files import ENUMS, PROXY, REGEX_MATCH_ENUM, REGEX_MATCH_PROXY


def download_file(url, filename):
    """
    Downloads a file from a given URL and saves it to a specified filename.
    """
    print(f"Downloading {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded successfully and saved as {filename}.")
    else:
        print(f"Failed to download {url}")


# The base URL of the website from which to scrape and download scripts
base_url = "https://swisstaxcalculator.estv.admin.ch"

# Regex pattern to match <script> tags with src attribute
pattern = re.compile(r'<script src="(\/.*?\.js)"><\/script>')

# Regex pattern to find the sourceMappingURL comment within JS files
pattern_sourcemap = re.compile(r"sourceMappingURL=(.*\.map)")

# Perform an initial request to get the page content
print(f"Fetching {base_url}...")
page_response = requests.get(base_url)

# Find all script tag matches
matches = pattern.findall(page_response.text)
sources = []  # List to hold tuples of script and its sourcemap URLs

if matches:
    print(f"Found {len(matches)} script(s). Processing...")
    for match in matches:
        filepath, filename = os.path.split(match)
        script_url = base_url + match
        script_response = requests.get(script_url)
        sourcemap_match = next(
            iter(pattern_sourcemap.findall(script_response.text)), None
        )

        if sourcemap_match:
            sourcemap_url = base_url + filepath + "/" + sourcemap_match
            sources.append((script_url, sourcemap_url))
else:
    print("No scripts found.")

# Create output directory if it doesn't exist
os.makedirs("out", exist_ok=True)

# Download each found script and its sourcemap
for script_url, sourcemap_url in sources:
    script_filename = "out/" + os.path.basename(script_url)
    sourcemap_filename = "out/" + os.path.basename(sourcemap_url)
    download_file(script_url, script_filename)
    download_file(sourcemap_url, sourcemap_filename)

# Run the reconstruct script using npm
print("Running the reconstruct script...")
subprocess.run(["npm", "run", "reconstruct"], shell=True)

# Convert selected enums to python classes
print("Converting enums...")
os.makedirs("out/converted/", exist_ok=True)
for filepath in ENUMS:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        if filepath == PROXY:
            proxy = next(
                iter(re.findall(REGEX_MATCH_PROXY, content, re.MULTILINE)), None
            )
    matches = re.findall(REGEX_MATCH_ENUM, content, re.MULTILINE)
    for match in matches:
        print(f"Creating {match[0]}")
        with open(f"out/converted/{match[0]}.py", "w", encoding="utf-8") as file:
            file.write(
                f"class {match[0]}: " + match[1].replace("//", "#").replace(",", "")
            )
with open("out/converted/__init__.py", "w", encoding="utf-8") as file:
    file.writelines([f'PROXY = "{proxy}"', f'BASE = "{base_url}"'])
