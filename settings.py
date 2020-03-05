import os
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    ENV = os.getenv("ENVIRONMENT")
    DEBUG = os.getenv('DEBUG')
