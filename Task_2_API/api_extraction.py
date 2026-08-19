import requests, json, csv, os

url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

os.makedirs("raw", exist_ok=True)

with open("raw/raw_api.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("api_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"API records extracted: {len(data)}")
print("Created: raw/raw_api.json")
print("Created: api_data.csv")