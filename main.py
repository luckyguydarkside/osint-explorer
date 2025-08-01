```python
import requests
import json

def fetch_ip_info(ip_address):
    """
    Fetches geolocation and other information about an IP address
    using the ipinfo.io API.

    Args:
        ip_address (str): The IP address to query.

    Returns:
        dict: A dictionary containing IP information if successful, 
              None otherwise.
    """
    try:
        # API endpoint for IP information
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        
        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data for IP {ip_address}, Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the fetched IP information in a readable format.

    Args:
        ip_info (dict): The dictionary containing IP information.
    """
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No information available.")

def main():
    """
    Main function to execute the OSINT script. 
    Prompts the user for an IP address and displays its information.
    """
    # User input for the IP address
    ip_address = input("Enter an IP address (or 'exit' to quit): ")
    
    if ip_address.lower() == 'exit':
        print("Exiting the program.")
        return
    
    # Fetch and display the IP information
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
