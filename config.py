import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Secure configuration management."""
    
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    
    @classmethod
    def validate(cls):
        """Validate all required secrets are configured."""
        if not cls.AWS_SECRET_KEY:
            raise ValueError("Missing required environment variables")
