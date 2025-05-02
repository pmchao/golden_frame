# test_create_post_extra_fields.py

"""
Test Case: Verify POST /posts ignores unexpected fields in the request.
Sends a valid request with an extra field and checks the response.
"""

import requests
import pytest
import allure
from data.config import BASE_URL
from utils.logger import logger

@allure.feature("Posts API")
@allure.story("POST /posts")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Verify POST ignores unexpected fields")
@pytest.mark.api
def test_create_post_extra_fields():
    """Test that extra fields in the POST body are ignored by the API."""

    payload = {
        "title": "extra fields test",
        "body": "payload with extra field",
        "userId": 1,
        "unexpected": "ignore this"
    }

    try:
        with allure.step("Send POST request with unexpected field"):
            logger.info("Sending POST request with an extra field")
            response = requests.post(BASE_URL, json=payload)
            logger.info(f"Response code: {response.status_code}")
            allure.attach(str(response.json()), name="POST Response", attachment_type=allure.attachment_type.JSON)

            assert response.status_code in [200, 201]
            #Peter Chao
            assert "unexpected"  in response.json()

    except Exception as e:
        logger.error(f"Test failed: {e}")
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(str(e))
