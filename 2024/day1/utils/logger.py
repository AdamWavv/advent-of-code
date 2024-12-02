import logging
import os

def get_logger(name):
    # Determine the path to the logs directory (one level up from the utils folder)
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)  # Ensure logs directory exists

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Handlers
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(os.path.join(log_dir, "app.log"))

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers if not already added
    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger