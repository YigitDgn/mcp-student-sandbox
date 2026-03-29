import os
from dotenv import load_dotenv

load_dotenv()

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def connect():
    if not AWS_SECRET_KEY:
        raise ValueError("AWS_SECRET_KEY not configured in environment")
    print("Connecting with configured credentials")
