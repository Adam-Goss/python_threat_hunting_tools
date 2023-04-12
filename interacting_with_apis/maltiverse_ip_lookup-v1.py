import json
from maltiverse import Maltiverse

# api = Maltiverse(auth_token="...")
api = Maltiverse()

while True:
    ip = input("Please enter IP to search for (or type exit to quit): ")
    ip_clean = str(ip).strip()

    if ip_clean == "quit":
        print("Goodbye.")
        break

    result = api.ip_get(ip)

    print(f"The IP address {ip_clean} has been identified as {result['classification']} by Malitverse")




       



