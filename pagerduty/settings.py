from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):

    db_uri: str
    db_schema: Optional[str]
    sms_endpoint: str = ""


settings = Settings()
