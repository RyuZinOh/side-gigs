import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

# Create a base directory to save images
base_dir = 'images'
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# URL of the website
url = 'https://new.oxfordcollege.edu.np/'

# Request the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags
images = soup.find_all('img')

# Download the images
for img in images:
    img_url = img.get('src')
    if img_url and (img_url.endswith('.jpg') or img_url.endswith('.png')):
        # Convert relative URLs to absolute
        img_url = urljoin(url, img_url)
        
        # Parse the URL to maintain folder structure
        parsed_url = urlparse(img_url)
        folder_structure = os.path.join(base_dir, os.path.dirname(parsed_url.path).lstrip('/'))

        # Create the necessary folders if they don't exist
        if not os.path.exists(folder_structure):
            os.makedirs(folder_structure)

        # Get the image filename and save it
        img_name = os.path.join(folder_structure, os.path.basename(parsed_url.path))
        img_data = requests.get(img_url).content
        with open(img_name, 'wb') as f:
            f.write(img_data)
        print(f'Downloaded {img_name}')
