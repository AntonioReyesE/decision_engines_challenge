"""
    Script that loads the environment variables for the app.
"""
from os.path import join, dirname
from dotenv import load_dotenv


def load_env():
    """
    Loads the environment variables
    """
    dotenv_path = join(dirname('backend'), '.env')
    load_dotenv(dotenv_path, override=True)
