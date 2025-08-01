```python
import requests

def fetch_ip_info(ip_address):
    """
    Fetches IP address information from an external API.
    
    Args:
        ip_address (str): The IP address to look up.
        
    Returns:
        dict: A dictionary containing IP information.
    """
    # Use the ipinfo.io API to get information about the IP address
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for IP: {ip_address} - Status Code: {response.status_code}")
        return None

def display_ip_info(ip_info):
    """
    Displays formatted information about the IP address.
    
    Args:
        ip_info (dict): The IP information dictionary.
    """
    if ip_info:
        print("IP Address Information:")
        print(f"IP: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
    else:
        print("No information available.")

def main():
    """
    Main function to run the OSINT IP lookup script.
    """
    # Example IP address for testing; can be modified or taken from user input
    ip_address = input("Enter an IP address to lookup: ")
    
    # Fetch and display IP information
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
