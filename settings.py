import os
from decouple import config

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORT = config('PORT', cast=int)
HOST = config('HOST')
