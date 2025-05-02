# test_api_delete.py

"""
Test Case: Verify DELETE /posts/{id} successfully deletes a post.
Includes Allure reporting, exception handling, and logging.
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from utils.logger import logger

@allure.feature("Posts API")
@allure.story("DELETE /posts/{id}")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify DELETE /posts/{id} deletes an existing post")
@pytest.mark.api
def test_delete_post():
    """Test that verifies a post can be created and then deleted."""

    try:
        with allure.step("Create a post to delete"):
            payload = {"title": "temporary post", "body": "to be deleted", "userId": 1}
            logger.info("Sending POST request to create a temporary post")
            response = requests.post(BASE_URL, json=payload)
            response.raise_for_status()
            post_id = response.json().get("id")
            logger.info(f"Post created with ID: {post_id}")
            allure.attach(str(response.json()), name="Created Post", attachment_type=allure.attachment_type.JSON)

        with allure.step(f"Send DELETE request to remove post ID {post_id}"):
            del_response = requests.delete(f"{BASE_URL}/{post_id}")
            logger.info(f"DELETE response status: {del_response.status_code}")
            assert del_response.status_code in [200, 204]

    except Exception as e:
        logger.error(f"Test failed due to: {e}")
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(str(e))
