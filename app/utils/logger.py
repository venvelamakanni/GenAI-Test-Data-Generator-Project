import sys
from pathlib import Path
from loguru import logger
from app.core.config import settings

# Remove default logger
logger.remove()

# Add console logger
logger.add(
    sys.stderr,
    format=settings.LOG_FORMAT,
    level=settings.LOG_LEVEL,
    colorize=True
)

# Add file logger with rotation
logger.add(
    settings.LOG_FILE,
    format=settings.LOG_FORMAT,
    level=settings.LOG_LEVEL,
    rotation=settings.LOG_MAX_SIZE,
    retention=settings.LOG_BACKUP_COUNT,
    compression="zip"
)

# Add error logger
error_log_file = settings.LOG_DIR / "error.log"
logger.add(
    error_log_file,
    format=settings.LOG_FORMAT,
    level="ERROR",
    rotation=settings.LOG_MAX_SIZE,
    retention=settings.LOG_BACKUP_COUNT,
    compression="zip"
)

# Add LLM interaction logger
llm_log_file = settings.LOG_DIR / "llm.log"
logger.add(
    llm_log_file,
    format=settings.LOG_FORMAT,
    level="DEBUG",
    rotation=settings.LOG_MAX_SIZE,
    retention=settings.LOG_BACKUP_COUNT,
    compression="zip",
    filter=lambda record: "llm" in record["extra"]
)

def get_logger(name: str):
    """Get a logger instance with the specified name."""
    return logger.bind(name=name) 