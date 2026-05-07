import requests

def get_json(url):
  """Takes a URL, and returns the JSON."""
  r = requests.get(url)
  print(f"GET request to {url} returned status code {r.status_code}")
  return r.json()