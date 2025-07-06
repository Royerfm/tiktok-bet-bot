# core/user_points.py
import json
import os

DATA_PATH = "data/points.json"

def load_data():
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump({}, f)
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def get_user_points(user):
    data = load_data()
    return data.get(user, 1000)  # todos inician con 1000 pts

def update_user_points(user, new_points):
    data = load_data()
    data[user] = get_user_points(user) + new_points
    save_data(data)
