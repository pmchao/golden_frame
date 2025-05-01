# test_api_posts.py

"""
Test Module: test_api_posts.py

This module contains automated API tests for verifying the functionality of
updating a post using the PUT /posts/{id} endpoint.

Features:
- Uses `requests` for API interaction
- Logs key actions and results
- Allure annotations for structured test reporting
- Exception handling for clear failure diagnostics

To Run:
    pytest --alluredir=allure-results
    allure serve allure-results
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from utils.logger import logger


@allure.feature("Posts API")
@allure.story("PUT /posts/{id}")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify PUT /posts/{id} updates the post title successfully")
@pytest.mark.api
def test_update_post():
    """Test to verify PUT /posts/{id} updates the post title successfully."""

    updated_data = {"title": "updated title"}
    post_id = 1
    endpoint = f"{BASE_URL}/{post_id}"

    logger.info("Starting test_update_post")
    logger.debug(f"Endpoint: {endpoint}")
    logger.debug(f"Payload: {updated_data}")

    try:
        with allure.step(f"Send PUT request to update post {post_id}"):
            response = requests.put(endpoint, json=updated_data)
            logger.info(f"PUT response status code: {response.status_code}")
            logger.debug(f"PUT response body: {response.text}")

        with allure.step("Verify response status code is 200"):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        with allure.step("Validate response content includes updated title"):
            data = response.json()
            allure.attach(str(data), name="Updated Response", attachment_type=allure.attachment_type.JSON)
            assert data.get("title") == "updated title", "Title was not updated as expected"

        logger.info("test_update_post PASSED")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        allure.attach(str(ae), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
        raise

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        allure.attach(str(e), name="Unexpected Exception", attachment_type=allure.attachment_type.TEXT)
        raise
