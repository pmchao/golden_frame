# test_get_post_invalid_id.py

"""
Test Case: Verify GET /posts/{id} returns a proper error for an invalid ID.
This test ensures the API handles non-existent resource access gracefully.
Uses logging, Allure steps, and exception handling.
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from utils.logger import logger

@allure.feature("Posts API")
@allure.story("GET /posts/{id}")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify GET /posts/{id} returns 404 or error for invalid ID")
@pytest.mark.api
def test_get_post_invalid_id():
    """Test that an invalid post ID returns appropriate error code."""

    invalid_id = 0  # Could also test with a very large ID like 999999

    try:
        with allure.step(f"Send GET request to retrieve non-existent post ID {invalid_id}"):
            logger.info(f"Sending request to fetch post with ID: {invalid_id}")
            response = requests.get(f"{BASE_URL}/{invalid_id}")
            logger.info(f"Received status code: {response.status_code}")
            allure.attach(str(response.text), name="Response Body", attachment_type=allure.attachment_type.TEXT)

            assert response.status_code in [404, 400]

    except Exception as e:
        logger.error(f"Test failed: {e}")
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(str(e))
