import requests
import time

def repeatedly_click_links(urls, repeat=10, delay=2):
    for url in urls:
        print(f"\nStarting requests for {url}...\n")
        for i in range(repeat):
            try:
                # Send an HTTP GET request to the URL
                response = requests.get(url)
                
                # Check if the request was successful
                if response.status_code == 200:
                    print(f"Request {i+1}: Successfully accessed {url}")
                else:
                    print(f"Request {i+1}: Failed to access {url}, Status Code: {response.status_code}")
                
                # Wait for the specified delay before sending the next request
                time.sleep(delay)
            
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while accessing {url}: {e}")
                break

# Example usage with multiple URLs
urls_to_click = [
    'https://bzn.li/5zpf3ir',
    'https://bzn.li/7g4hRiz',
    'https://bzn.li/MxYs4ir',
    'https://bzn.li/16BU7ig',
]

repeatedly_click_links(urls_to_click, repeat=10000, delay=1)
