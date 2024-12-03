# Define the __all__ variable
__all__ = ["dirname","basename","isfile","load_config","connect","main","insert_data","Scrape"]

from os.path import dirname, basename, isfile
from .config import load_config
from .connect import connect
from .execute import set_table, insert_data
from .scrape import Scrape

__version__ = "2.11.4"

