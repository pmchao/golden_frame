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

def run_all_tests():
    try:
        print("Running tests...")
        subprocess.run(["pytest", "--alluredir=allure-results"], check=True)

        print("Launching Allure report (will auto-close in 10 seconds)...")
        proc = subprocess.Popen(["allure", "serve", "allure-results"])

        print("Launching Allure report (will auto-close in 10 seconds)...")
        for i in range(10, 0, -1):
            print(f"Closing in {i} seconds...", end='\r')
            time.sleep(1)

        print("Stopping Allure server gracefully...")
        proc.terminate()  # Just stop the allure server, not the whole terminal
        proc.wait(timeout=5)

    except subprocess.CalledProcessError as e:
        print(f"Test execution failed: {e}")
    except FileNotFoundError as e:
        print("Allure CLI not found. Make sure it’s installed and in PATH.")
        print(f"System error: {e}")
    except subprocess.TimeoutExpired:
        print("Allure server did not shut down in time, forcing close.")
        proc.kill()

if __name__ == "__main__":
    run_all_tests()
