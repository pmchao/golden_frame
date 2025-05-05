"""
run_tests.py

Purpose:
    Runs pytest-based API tests and shows the Allure report for 10 seconds,
    then gracefully stops the Allure server without closing PyCharm or terminal.

Usage:
    python run_tests.py
"""

import subprocess
import time
import logging

# Configure logging
logging.basicConfig(
    filename="run_tests.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def run_all_tests():
    try:
        logging.info("Starting test execution...")
        print("Running tests...")
        subprocess.run(["pytest", "--alluredir=allure-results"], check=True)
        logging.info("Pytest execution completed successfully.")

        logging.info("Launching Allure report server...")
        print("Launching Allure report (will auto-close in 10 seconds)...")
        proc = subprocess.Popen(["allure", "serve", "allure-results"])

        for i in range(10, 0, -1):
            print(f"Closing in {i} seconds...", end='\r')
            time.sleep(1)

        logging.info("Stopping Allure report server...")
        print("Stopping Allure server gracefully...")
        proc.terminate()
        proc.wait(timeout=5)
        logging.info("Allure server stopped successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Test execution failed: {e}")
        print(f"Test execution failed: {e}")
    except FileNotFoundError as e:
        logging.critical("Allure CLI not found. Make sure it’s installed and in PATH.")
        logging.critical(f"System error: {e}")
        print("Allure CLI not found. Make sure it’s installed and in PATH.")
        print(f"System error: {e}")
    except subprocess.TimeoutExpired:
        logging.warning("Allure server did not shut down in time, forcing close.")
        proc.kill()
        logging.info("Allure server was killed forcefully.")

if __name__ == "__main__":
    run_all_tests()
