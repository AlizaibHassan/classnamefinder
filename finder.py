import requests
from bs4 import BeautifulSoup

# Function to check if page source contains class "media__placeholder"
def has_media_placeholder(url):
    headers = {
        'User-Agent': 'Your User-Agent Here',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find(class_="media__placeholder") is not None
    return False

# Read URLs from input.txt
with open('input.txt', 'r') as file:
    urls = file.readlines()

# Check each URL and save to output.txt if condition is met
with open('output.txt', 'w') as output_file:
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespaces
        if has_media_placeholder(url):
            output_file.write(url + '\n')

print("Task completed. Check output.txt for the result.")
