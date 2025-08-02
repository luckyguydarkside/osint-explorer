```python
import requests

def fetch_ip_info(ip_address):
    """
    Fetches geolocation and ISP information for a given IP address using the ipinfo.io API.

    Args:
        ip_address (str): The IP address to lookup.

    Returns:
        dict: A dictionary containing the IP information or an error message.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response as a dictionary
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}  # Return the error message

def display_ip_info(ip_info):
    """
    Displays the information of the IP address in a readable format.

    Args:
        ip_info (dict): The dictionary containing IP information.
    """
    if "error" in ip_info:
        print(f"Error fetching IP info: {ip_info['error']}")
    else:
        print(f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")

def main():
    """
    Main function to execute the OSINT IP lookup project.
    Prompts user for an IP address and displays its information.
    """
    ip_address = input("Enter an IP address to lookup: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()  # Start the OSINT project
```