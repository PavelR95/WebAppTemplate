from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Common settings
    DEBUG: bool = True
    TITLE: str = "WebAppTemplate"
    DESCRIPTION: str = "Application description"
    VERSION: str = "v0.0.1"

    # Logger settings
    log_level: str = "INFO"
    log_message_format: str = "%(asctime)s - %(name)s [%(levelname)s] - %(message)s"
    log_datetime_format: str = "%Y-%m-%d %H:%M:%S"

    # App settings

    # Server settings
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    server_reload: bool = True
    server_factory: bool = True
    server_workers_default: int = 1

    @property
    def server_workers(self):
        if self.server_reload is True:
            return None
        else:
            return self.server_workers_default

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
    )


settings = Settings()
