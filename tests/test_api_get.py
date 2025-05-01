import pytest
import allure
from api_controller import posts_api
from utils.logger import logger
from data.config import BASE_URL

@allure.feature("Posts API ")
@allure.story("GET /posts")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify GET /posts returns a list of posts and 200 status code")
def test_get_all_posts():
    """Test that validates the /posts endpoint and logs errors cleanly."""

    logger.info("Starting test: test_get_all_posts")

    try:
        with allure.step("Send GET request to /posts endpoint"):
            response = posts_api.get_all_posts()
            logger.info(f"GET   /posts responded with status code: {response.status_code}")

        with allure.step("Verify status code is 200"):
            assert response.status_code == 200

        with allure.step("Verify response is a list"):
            posts = response.json()
            assert isinstance(posts, list)
            logger.info(f"Received {len(posts)} posts")

        logger.info("test_get_all_posts PASSED")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        allure.attach(str(ae), name="Assertion Error", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to assertion error: {ae}")

    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")
        allure.attach(str(e), name="Unexpected Error", attachment_type=allure.attachment_type.TEXT)
        pytest.fail(f"Test failed due to unexpected exception: {e}")
