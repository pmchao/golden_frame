import pytest
from api_controller import posts_api
from utils.logger import logger  # <-- import your shared logger

def test_get_all_posts():
    logger.info("Starting test: test_get_all_posts")

    response = posts_api.get_all_posts()
    logger.info(f"GET /posts responded with status code: {response.status_code}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

    logger.info(f"Received {len(response.json())} posts")
    logger.info("test_get_all_posts PASSED")
    print(response.json())  # Optional, mostly for dev time
