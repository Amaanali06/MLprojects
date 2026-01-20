import os
import logging
from datetime import datetime

# 1. Create logs directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# 2. Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 3. Full log file path (DIRECT FILE, NOT FOLDER)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# 4. Logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
