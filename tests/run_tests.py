"""
run_tests.py

Purpose:
    Acts as a driver script to automate running all pytest-based API tests
    and generating an Allure report.

Features:
    - Executes all tests using pytest
    - Stores test results in the 'allure-results' folder
    - Serves the Allure report in the browser automatically

Requirements:
    - pytest
    - allure-pytest
    - Allure command-line tool installed and in PATH

Usage:
    python run_tests.py
"""

import subprocess

def run_all_tests():
    try:
        print("Running tests...")
        subprocess.run(["pytest", "--alluredir=allure-results"], check=True)

        print("Launching Allure report...")
        subprocess.run(["allure", "serve", "allure-results"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred during test execution: {e}")
    except FileNotFoundError as e:
        print("Make sure Allure is installed and in your system PATH.")
        print(f"System error: {e}")

if __name__ == "__main__":
    run_all_tests()
