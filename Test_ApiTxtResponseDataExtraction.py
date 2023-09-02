import requests

url = "https://timesofindia.indiatimes.com/ads.txt"

response = requests.get(url)
#print(response.text)

if response.status_code == 200:
    content = response.text

    # Process the content pubmatic
    dic1 = {}
    lines = content.split('\n')
    for line in lines:
        if line.startswith("#"):
            continue
        parts = line.split(', ')
        if len(parts) >= 4:
            key = parts[0] + " " + parts[2]
            #print(key)
            value = parts[3]
            #print(value)
            if parts[0] + " " + parts[2] not in dic1:
                dic1.update({key: value})

    print("Dictionary :", dic1)

else:
    print(f"Request failed with status code: {response.status_code}")

