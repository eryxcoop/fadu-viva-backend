import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    ENV = os.getenv("ENVIRONMENT")
    HERE_API_KEY = os.getenv('HERE_API_KEY')
    CACHE_SERVER = (os.getenv("CACHE_SERVER_HOST"), int(os.getenv("CACHE_SERVER_PORT")))
    BSAS_TRANSPORT_API_CLIENT_ID = os.getenv('BSAS_TRANSPORT_API_CLIENT_ID')
    BSAS_TRANSPORT_API_SECRET = os.getenv('BSAS_TRANSPORT_API_SECRET')

    @classmethod
    def for_actual_environment(cls):
        all_config_objects = [DevelopmentConfig, ProductionConfig]
        for config_object in all_config_objects:
            if config_object.is_correct_for(cls.ENV):
                return config_object

        all_environments_names = ', '.join(config.environment_name() for config in all_config_objects)
        raise Exception(f"No config found for environment: {cls.ENV}. Available environments: {all_environments_names}")

    @classmethod
    def is_correct_for(cls, environment_name):
        raise NotImplementedError

    @classmethod
    def environment_name(cls):
        raise NotImplementedError

    @classmethod
    def get_cache_client(cls, cache_factory):
        raise NotImplementedError


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def environment_name(cls):
        return 'development'

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == cls.environment_name()

    @classmethod
    def get_cache_client(cls, cache_factory):
        return cache_factory.memcached_client(server=cls.CACHE_SERVER)


class ProductionConfig(Config):
    DEBUG = False

    @classmethod
    def environment_name(cls):
        return 'production'

    @classmethod
    def is_correct_for(cls, environment_name):
        return environment_name == cls.environment_name()

    @classmethod
    def get_cache_client(cls, cache_factory):
        return cache_factory.memcached_client(server=cls.CACHE_SERVER)


app_config = Config.for_actual_environment()
