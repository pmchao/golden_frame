# test_api_posts.py

"""
Test Module: test_api_posts.py

Verifies that the POST /posts endpoint can successfully create a new post.
Includes logging, exception handling, and Allure reporting.

To run:
    pytest --alluredir=allure-results
    allure serve allure-results
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from data.test_data import new_post_data  # <-- Import the test data
from utils.logger import logger


@allure.feature("Posts API")
@allure.story("POST /posts")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify POST /posts creates a new post with correct data")
@pytest.mark.api
def test_create_post():
    """Test to verify a POST request creates a new post with correct data."""

    logger.info("Starting test_create_post")
    logger.debug(f"Payload to be sent: {new_post_data}")

    try:
        with allure.step("Send POST request to /posts endpoint"):
            response = requests.post(BASE_URL, json=new_post_data)
            logger.info(f"POST status code: {response.status_code}")
            logger.debug(f"POST response body: {response.text}")

        with allure.step("Verify status code is 201"):
            assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        with allure.step("Parse and validate response JSON"):
            data = response.json()
            allure.attach(str(data), name="Response JSON", attachment_type=allure.attachment_type.JSON)

            assert data["title"] == new_post_data["title"], "Title mismatch"
            assert data["body"] == new_post_data["body"], "Body mismatch"
            assert data["userId"] == new_post_data["userId"], "User ID mismatch"

        logger.info("test_create_post PASSED")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        allure.attach(str(ae), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
        raise

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        allure.attach(str(e), name="Unexpected Exception", attachment_type=allure.attachment_type.TEXT)
        raise
