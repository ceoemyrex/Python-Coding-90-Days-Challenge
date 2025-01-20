#- Project:
# Write a program that interacts with the GitHub API to fetch user data (like profile information).


import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_github_user(ceoemyrex, token=None):
    """Fetches GitHub user data using the GitHub API.

    Args:
        username: The GitHub username.
        token: (Optional) A GitHub Personal Access Token for authenticated requests.

    Returns:
        A dictionary containing user data, or None if an error occurs.
        Prints an error message to the console if there is an error.
    """
    base_url = f"https://api.github.com/users/{ceoemyrex}"
    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        user_data = response.json()
        return user_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        if response.status_code == 404:
            print(f"User '{username}' not found.")
        elif response.status_code == 403:
            print("Rate limit exceeded or invalid token.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def display_user_info(user_data):
    """Displays formatted GitHub user information.

    Args:
        user_data: The dictionary containing the user data.
    """
    if user_data:
        print(f"Username: {user_data.get('login', 'N/A')}")
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Bio: {user_data.get('bio', 'N/A')}")
        print(f"Location: {user_data.get('location', 'N/A')}")
        print(f"Public Repositories: {user_data.get('public_repos', 'N/A')}")
        print(f"Followers: {user_data.get('followers', 'N/A')}")
        print(f"Following: {user_data.get('following', 'N/A')}")
        print(f"Profile URL: {user_data.get('html_url', 'N/A')}")
        print(f"Avatar URL: {user_data.get('avatar_url', 'N/A')}")
    else:
        print("No user data to display.")

if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TOKEN")  # Get token from environment variable
    if not github_token:
        print("Warning: GITHUB_TOKEN environment variable not set. Making unauthenticated requests (rate limits apply).")

    try:
        username = input("Enter a GitHub username: ")
        user_info = get_github_user(username, github_token)
        display_user_info(user_info)
    except EOFError:
        print("\nInput ended.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred during input: {e}")