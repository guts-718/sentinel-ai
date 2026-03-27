import os

def get_env(key: str) -> str:
    value = os.getenv(key)

    if value is None or value.strip() == "":
        raise ValueError(f"❌ Missing required environment variable: {key}")

    return value