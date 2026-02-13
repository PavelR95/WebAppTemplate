from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Настройки логирования
    log_level: str = "INFO"
    log_message_format: str = "%(asctime)s - %(name)s [%(levelname)s] - %(message)s"
    log_datetime_format: str = "%Y-%m-%d %H:%M:%S"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
    )


settings = Settings()
