import os
import logging

# Create a directory for log files if it doesn't exist
log_path = 'logs'
os.makedirs(log_path, exist_ok=True)

# Set up logging
logging.basicConfig(
    filename=os.path.join(log_path, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)