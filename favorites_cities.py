import json
import os

FAV_FILE = 'favorites.json'

def load_favorites():
    if not os.path.exists(FAV_FILE):
        return []
    with open(FAV_FILE, 'r') as f:
        data = json.load(f)
        return data.get("favorites", [])

def save_favorites(favorites):
    with open(FAV_FILE, 'w') as f:
        json.dump({"favorites": favorites}, f, indent=4)

def add_favorite(city):
    favorites = load_favorites()
    city = city.strip().title()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        return True
    return False

def remove_favorite(city):
    favorites = load_favorites()
    city = city.strip().title()
    if city in favorites:
        favorites.remove(city)
        save_favorites(favorites)
