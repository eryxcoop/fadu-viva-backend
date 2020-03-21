import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    ENV = os.getenv("ENVIRONMENT")

    @classmethod
    def for_actual_environment(cls):
        all_config_objects = [TestConfig, DevelopmentConfig]
        for config_object in all_config_objects:
            if config_object.is_correct_for(cls.ENV):
                return config_object

        return DevelopmentConfig


class TestConfig(Config):
    TESTING = True
    ENV = os.getenv("ENVIRONMENT")

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == 'testing'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = os.getenv("ENVIRONMENT")
    HERE_API_KEY = os.getenv('HERE_API_KEY')

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == 'development'


app_config = Config.for_actual_environment()
