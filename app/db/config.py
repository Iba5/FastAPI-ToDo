from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    database_url:str
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

Config = Settings() # type: ignore


"""
BaseSettings:
-> We import BaseSettings from Pydantic.
-> Any class that inherits from BaseSettings automatically gains the ability to read values from environment files (like .env).
-> This tells us that the class is meant to hold configuration settings, such as database credentials.
-> We then create an instance of the class, which loads the database URL and other secrets we’ve hidden in the .env file.

SettingsConfigDict:
-> We import SettingsConfigDict to configure how Pydantic reads environment settings.
-> It helps locate the .env file where we store secret values (e.g., database URLs) so they aren’t exposed in the code.
-> It also clarifies which environment is being used and defines behaviors like ignoring extra fields. 
"""