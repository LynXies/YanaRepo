import sqlite3
from bs4 import BeautifulSoup
import pandas as pd


conn = sqlite3.connect('lab.db')
cursor = conn.cursor()
