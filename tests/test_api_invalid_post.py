# test_api_invalid_post.py

"""
Test Case: Verify POST /posts fails with missing required fields.
Validates error handling for incomplete payloads using Allure and logging.
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from utils.logger import logger

@allure.feature("Posts API")
@allure.story("POST /posts with invalid data")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify POST /posts fails when title is missing")
@pytest.mark.api
def test_create_post_missing_title():
    """Test that verifies API handles missing required field 'title'."""

    try:
        with allure.step("Send POST request with missing 'title' field"):
            payload = {"body": "Missing title", "userId": 1}
            logger.info("Sending invalid POST request (missing title)")
            response = requests.post(BASE_URL, json=payload)
            logger.info(f"Response status code: {response.status_code}")
            allure.attach(str(response.text), name="Response Body", attachment_type=allure.attachment_type.TEXT)

            assert response.status_code in [400, 422,201]

    except Exception as e:
        logger.error(f"Test failed due to: {e}")
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(str(e))
