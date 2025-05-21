from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "GenAI Test Data Generator"
    
    # LLM Settings
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-2.0-flash"
    MAX_BATCH_SIZE: int = 5
    
    # Logging Settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_DIR: Path = Path("logs")
    LOG_FILE: Path = LOG_DIR / "app.log"
    LOG_MAX_SIZE: int = 10 * 1024 * 1024  # 10MB
    LOG_BACKUP_COUNT: int = 5
    
    # Test Settings
    TEST_SCENARIO_TYPES: List[str] = [
        "POSITIVE",
        "NEGATIVE",
        "EDGE_CASE",
        "PERFORMANCE",
        "SECURITY"
    ]
    
    # File Paths
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    STATIC_DIR: Path = BASE_DIR / "static"
    TESTS_DIR: Path = BASE_DIR / "tests"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# Create necessary directories
settings.LOG_DIR.mkdir(exist_ok=True)
settings.STATIC_DIR.mkdir(exist_ok=True)
settings.TESTS_DIR.mkdir(exist_ok=True) 