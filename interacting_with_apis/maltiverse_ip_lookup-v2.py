import json
import requests


url = 'https://api.maltiverse.com/ip/'

while True:
    ip = input("Please enter IP to search for (or type exit to quit): ")
    ip_clean = str(ip).strip()
    
    if ip_clean == "quit":
        print("Goodbye.")
        break

    response = requests.get(url + ip)
    result = json.loads(response.text)
    
    print(f"The IP address {ip_clean} has been identified as {result['classification']} by Malitverse")




       



