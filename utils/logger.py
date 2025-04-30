import logging
import os

# Ensure a logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/test_run.log",
    filemode="a",  # Append mode
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Create and export a reusable logger
logger = logging.getLogger("api_test_logger")
