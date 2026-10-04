#Scripts that works top-bottom receiving an input, processing it sequentially and then outputing something valuable.
#It is lightweight and not like massive interating modules.
from urllib.parse import urlparse
import requests

def is_valid_url(url):
    try:
        result = urlparse(url)
        
        return all([result.scheme in ['http', 'https'], result.netloc])
    except ValueError:
        return False


article_url = input("Enter the URL: ")




#Local Validation
if not is_valid_url(article_url):
    print(f"Error: '{article_url}' is not a valid website URL. Please try again with http:// or https://")
    
else:
    #Later the LLM is going to get triggered right here!
    print("Valid URL structure, Attempting to fetch the webpage...")

    #our browser is the client talking to WEBSERVER hosting that URL.
    try:
        # We add a common 'User-Agent' header so servers don't mistake our script for an aggressive bot
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        # Send the GET request with a 10-second timeout limit
        response = requests.get(article_url, headers=headers, timeout=10)
        
        # This checks the HTTP status code
        response.raise_for_status()
        
        print("✅ Success! Webpage downloaded.")
        print("-" * 50)
        # Print the first 500 characters of the raw HTML data we just retrieved
        print(response.text[:500]) 
        print("-" * 50)
        
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP Error occurred: {http_err}")  # e.g., 404 Not Found
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not connect to the server. Check your internet or the domain name.")
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The server took too long to respond.")
    except requests.exceptions.RequestException as err:
        print(f"❌ An unexpected network error occurred: {err}")