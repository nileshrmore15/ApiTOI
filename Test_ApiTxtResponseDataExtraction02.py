import requests

url = "https://timesofindia.indiatimes.com/ads.txt"

response = requests.get(url)
#print(response.text)

if response.status_code == 200:
    content = response.text

    # Process the content pubmatic
    lines = content.split('\n')
    for line in lines:
        if line.startswith("#"):
            continue
        parts = line.split(', ')
        if len(parts) >= 4:
            domain = parts[0]
            publisher_id = parts[1]
            relationship = parts[2]
            key = parts[3]
            print(f"Domain: {domain}, Publisher ID: {publisher_id}, Relationship: {relationship}, Key: {key}")
else:
    print(f"Request failed with status code: {response.status_code}")

