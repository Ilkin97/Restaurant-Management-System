import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

env = os.getenv("DJANGO_ENV")

if env == "prod":
    from .prod import *
else:
    from .dev import *
