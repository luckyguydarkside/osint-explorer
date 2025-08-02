```python
import requests
import json

def get_ip_info(ip_address):
    """
    Fetches information about a given IP address using ipinfo.io API.
    
    :param ip_address: str - The IP address to look up.
    :return: dict - A dictionary containing IP information or an error message.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response as a dictionary
    except requests.RequestException as e:
        return {"error": str(e)}  # Handle any request exceptions

def display_ip_info(ip_info):
    """
    Displays the IP information in a readable format.
    
    :param ip_info: dict - The dictionary containing IP information.
    """
    if 'error' in ip_info:
        print(f"Error: {ip_info['error']}")
    else:
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")

def main():
    """
    Main function to run the OSINT IP information retrieval.
    It prompts the user for an IP address and displays the information.
    """
    ip_address = input("Enter an IP address to lookup: ")
    ip_info = get_ip_info(ip_address)  # Get IP information
    display_ip_info(ip_info)  # Display the information

if __name__ == "__main__":
    main()  # Run the main function
```