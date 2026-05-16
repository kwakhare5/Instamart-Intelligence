from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    MCP_BASE_URL: str = 'http://localhost:3001'
    ANTHROPIC_API_KEY: str
    TWILIO_ACCOUNT_SID: str = ''
    TWILIO_AUTH_TOKEN: str = ''
    TWILIO_WHATSAPP_FROM: str = ''
    ALERT_THRESHOLD_DAYS: int = 2
    MIN_CONFIDENCE: float = 0.50

    class Config:
        env_file = '.env'


settings = Settings()
