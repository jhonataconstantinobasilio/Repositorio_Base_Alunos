import requests

r = requests.get('https://catfact.ninja/fact ')
j = r.json()

print(j.get("f"))