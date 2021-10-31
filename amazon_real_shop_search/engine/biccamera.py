import os
import csv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import requests
from bs4 import BeautifulSoup
from logger import set_logger
import pandas as pd

logger = set_logger(__name__)

def fetch_biccamera_data():
    