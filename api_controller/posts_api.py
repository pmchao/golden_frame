import requests
from data.config import BASE_URL

def get_all_posts():
    """Fetch all posts."""
    return requests.get(BASE_URL)

def get_post_by_id(post_id):
    """Fetch a single post by ID."""
    return requests.get(f"{BASE_URL}/{post_id}")

def create_post(data):
    """Create a new post."""
    return requests.post(BASE_URL, json=data)

def update_post(post_id, data):
    """Update an existing post."""
    return requests.put(f"{BASE_URL}/{post_id}", json=data)

def delete_post(post_id):
    """Delete a post."""
    return requests.delete(f"{BASE_URL}/{post_id}")
