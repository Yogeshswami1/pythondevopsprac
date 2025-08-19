import requests

# BASE_URL = "http://localhost:8000/api/notes/"

BASE_URL = "http://52.66.171.14/api/notes/"


def get_notes():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    return []

def add_note(title, content):
    payload = {"title": title, "content": content}
    response = requests.post(BASE_URL, json=payload)
    return response.status_code == 201
