# Project:
# Create a program that scrapes a website (e.g., news headlines from a news site) and displays the results.


import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    """
    Scrapes news headlines from a given URL.

    Args:
        url: The URL of the website to scrape.

    Returns:
        A list of news headlines, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")

        headlines = []
        # This part is highly website-specific. Inspect the target website's HTML
        # to find the correct tags and classes that contain the headlines.
        # Examples below, you'll likely need to adjust this.

        # Example 1: Finding headlines within <h2> tags with a specific class
        for headline_tag in soup.find_all("h2", class_="headline"):
            headlines.append(headline_tag.text.strip())

        # Example 2: Finding headlines within <a> tags inside a <div> with a specific ID
        for headline_tag in soup.find("div", id="news-container").find_all("a"):
            headlines.append(headline_tag.text.strip())

        # Example 3: Finding headlines within <h3> tags
        for headline_tag in soup.find_all("h3"):
            headlines.append(headline_tag.text.strip())

        if not headlines: #If no headlines are found using the provided selectors, warn the user.
            print("Warning: No headlines found. Please inspect the website's HTML and update the selectors.")

        return headlines

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except AttributeError as e: #Handle cases where find() returns None
        print(f"Error parsing HTML: {e}. Likely the HTML structure changed or the selectors are incorrect.")
        return None



if __name__ == "__main__":
    target_url = input("Enter the URL of the news website: ")
    if not target_url.startswith("http"): #Add http if user forgets
        target_url = "https://" + target_url
    headlines = scrape_news_headlines(target_url)

    if headlines:
        print("\nNews Headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")