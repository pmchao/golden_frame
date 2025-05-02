# test_api_get_single_post.py

"""
Test Case: Verify GET /posts/{id} successfully retrieves a single post.
Uses logging and Allure for structured reporting.
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from utils.logger import logger

@allure.feature("Posts API")
@allure.story("GET /posts/{id}")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify GET /posts/{id} returns a valid post")
@pytest.mark.api
def test_get_single_post():
    """Test that retrieves a single post by ID and checks response structure."""

    post_id = 1
    try:
        with allure.step(f"Send GET request to retrieve post ID {post_id}"):
            response = requests.get(f"{BASE_URL}/{post_id}")
            logger.info(f"GET /posts/{post_id} status: {response.status_code}")
            allure.attach(str(response.json()), name="Post Response", attachment_type=allure.attachment_type.JSON)

            assert response.status_code == 200
            assert response.json().get("id") == post_id

    except Exception as e:
        logger.error(f"Test failed due to: {e}")
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(str(e))
