import requests
import os
from dotenv import load_dotenv

#Loading .env
load_dotenv()

# credential
USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')

# github apis urls
API_BASE_URL = "https://api.github.com"
FOLLOWERS_API = f"{API_BASE_URL}/users/{USERNAME}/followers"
FOLLOWING_API = f"{API_BASE_URL}/users/{USERNAME}/following"
UNFOLLOW_API = f"{API_BASE_URL}/user/following"

# Function to fetch data from GitHub API
def get_data(url):
    response = requests.get(url, auth=(USERNAME, TOKEN))
    if response.status_code == 200:
        return [user['login'] for user in response.json()]
    else:
        print(f"Failed to fetch data from {url}: {response.status_code} - {response.text}")
        return []

# Function to unfollow a user
def unfollow_user(username):
    url = f"{UNFOLLOW_API}/{username}"
    response = requests.delete(url, auth=(USERNAME, TOKEN))
    if response.status_code == 204:
        print(f"Unfollowed {username}")
    else:
        print(f"Failed to unfollow {username}: {response.status_code} - {response.text}")
